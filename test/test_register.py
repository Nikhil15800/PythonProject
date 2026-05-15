from ..pages.registerPage import Register
import pytest
from ..config import Config

@pytest.mark.order(1)
def testgoToRegisterPage(driver):
    callRegisterPage = Register(driver)
    callRegisterPage.goToRegisterPage()

@pytest.mark.order(2)
def testRegister(driver):
    callRegisterPage = Register(driver)
    callRegisterPage.register(Config.USERNAME, Config.EMAIL)

@pytest.mark.order(3)
def testEnterAccountInformation(driver):
    callRegisterPage = Register(driver)
    # Add code to enter account information and assert the expected outcome         
    callRegisterPage.enterAccountInformation(
        password=Config.PASSWORD,
        day="1",
        month="1",
        year="2000",
        firstName="Test",
        lastName="User",
        company="Test Company",
        address1="123 Test St",
        address2="Apt 4",
        country="United States",
        state="Test State",
        city="Test City",
        zipcode="12345",
        mobileNumber="1234567890"
    )

@pytest.mark.order(4)
def testverifyAccountCreated(driver):
    callRegisterPage = Register(driver)
    accountText = callRegisterPage.verifyAccountCreated()
    print(f"Actual text: '{accountText}'")
    assert accountText.lower() == "account created!", f"Expected 'Account Created!', got '{accountText}'"