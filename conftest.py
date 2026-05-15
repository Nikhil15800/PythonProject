import pytest
from selenium import webdriver
from .config import Config
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test_log.log", mode='w'),
        logging.StreamHandler()
    ]
)

@pytest.fixture(scope="session")
def driver():
    logger = logging.getLogger("conftest")
    logger.info("Starting Chrome driver")
    driver = webdriver.Chrome()  # You can specify the path to chromedriver if it's not in your PATH
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    logger.info(f"Navigated to {Config.BASE_URL}")
    yield driver
    logger.info("Quitting driver")
    driver.quit()


def pytest_collection_modifyitems(session, config, items):
    def order_key(item):
        marker = item.get_closest_marker("order")
        if marker is not None and marker.args:
            try:
                return int(marker.args[0])
            except (TypeError, ValueError):
                return float("inf")
        return float("inf")

    items.sort(key=order_key)
