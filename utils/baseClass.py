from selenium.webdriver.common.by import By
import logging

class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def getTitle(self):
        title = self.driver.title
        self.logger.info(f"Page title: {title}")
        return title
    
    def getCurrentURL(self):
        url = self.driver.current_url
        self.logger.info(f"Current URL: {url}")
        return url
    
    def findElement(self, by, value):
        self.dismissAdPopupIfPresent()
        element = self.driver.find_element(by, value)
        self.logger.info(f"Found element: {by}={value}")
        return element
    
    def clickElement(self, by, value):
        self.findElement(by, value).click()
        self.logger.info(f"Clicked element: {by}={value}")

    def clickElementJS(self, by, value):
        element = self.findElement(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", element)
        self.logger.info(f"JS clicked element: {by}={value}")

    def sendKeys(self, by, value, text):
        self.findElement(by, value).send_keys(text)
        self.logger.info(f"Sent keys '{text}' to element: {by}={value}")

    def isElementPresent(self, by, value):
        try:
            self.findElement(by, value)
            return True
        except:
            return False

    def dismissAdPopupIfPresent(self):
        popup_selectors = [
            (By.ID, "dismiss-button-element"),
        ]
        for by, value in popup_selectors:
            elements = self.driver.find_elements(by, value)
            if elements:
                for popup_close in elements:
                    try:
                        if popup_close.is_displayed() and popup_close.is_enabled():
                            popup_close.click()
                            self.logger.info(f"Dismissed ad popup: {by}={value}")
                            return True
                    except Exception as e:
                        self.logger.warning(f"Could not click ad popup close button {by}={value}: {e}")
                        try:
                            self.driver.execute_script("arguments[0].click();", popup_close)
                            self.logger.info(f"Dismissed ad popup with JS click: {by}={value}")
                            return True
                        except Exception as js_e:
                            self.logger.warning(f"JS click also failed for ad popup {by}={value}: {js_e}")
        try:
            dismissed = self.driver.execute_script(
                "var el = document.getElementById('dismiss-button-element'); if (el) { el.click(); return true; } return false;"
            )
            if dismissed:
                self.logger.info("Dismissed ad popup using JavaScript selector")
                return True
        except Exception as e:
            self.logger.debug(f"JavaScript popup dismissal check failed: {e}")
        return False
        
    def waitForElement(self, by, value, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        def _element_present(driver):
            self.dismissAdPopupIfPresent()
            try:
                element = driver.find_element(by, value)
                if element.is_displayed():
                    return element
                return False
            except Exception as e:
                self.logger.debug(f"Waiting for element {by}={value}: {e}")
                return False

        return WebDriverWait(self.driver, timeout).until(_element_present)

    def getElementText(self, by, value):
        return self.findElement(by, value).text
    
    def getElementAttribute(self, by, value, attribute):
        return self.findElement(by, value).get_attribute(attribute)
    
    def isElementDisplayed(self, by, value):
        return self.findElement(by, value).is_displayed()
    
    def isElementEnabled(self, by, value):
        return self.findElement(by, value).is_enabled()
    
    def isElementSelected(self, by, value):
        return self.findElement(by, value).is_selected()
    
    def selectDropdownByVisibleText(self, by, value, text):
        from selenium.webdriver.support.ui import Select
        select = Select(self.findElement(by, value))
        select.select_by_visible_text(text) 

    def selectDropdownByValue(self, by, value, option_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.findElement(by, value))
        select.select_by_value(option_value)

    def selectDropdownByIndex(self, by, value, index):
        from selenium.webdriver.support.ui import Select
        select = Select(self.findElement(by, value))
        select.select_by_index(index)

    def getAllDropdownOptions(self, by, value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.findElement(by, value))
        return [option.text for option in select.options]
    
    def getSelectedDropdownOption(self, by, value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.findElement(by, value))
        return select.first_selected_option.text
    
    def switchToFrame(self, by, value):
        self.driver.switch_to.frame(self.findElement(by, value))

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def switchToAlert(self):
        return self.driver.switch_to.alert  
    
    def acceptAlert(self):
        self.switchToAlert().accept()   

    def dismissAlert(self):
        self.switchToAlert().dismiss()

    def getAlertText(self):
        return self.switchToAlert().text
    
    def sendKeysToAlert(self, text):
        self.switchToAlert().send_keys(text)

    def switchToWindow(self, index):
        windows = self.driver.window_handles
        if index < len(windows):
            self.driver.switch_to.window(windows[index])
        else:
            raise IndexError("Invalid window index")
        
    def closeCurrentWindow(self):
        self.driver.close() 

    def maximizeWindow(self):
        self.driver.maximize_window()   

    def minimizeWindow(self):
        self.driver.minimize_window()   

    def refreshPage(self):
        self.driver.refresh()   

    def navigateToURL(self, url):
        self.driver.get(url)

    def getPageSource(self):
        return self.driver.page_source
    
    def getCookies(self):
        return self.driver.get_cookies()
    
    def addCookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def deleteCookie(self, name):
        self.driver.delete_cookie(name)
    def deleteAllCookies(self):
        self.driver.delete_all_cookies()

    def executeJavaScript(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    def takeScreenshot(self, file_path):
        self.driver.save_screenshot(file_path) 
    
    def getElementCount(self, by, value):
        return len(self.driver.find_elements(by, value))    
    
