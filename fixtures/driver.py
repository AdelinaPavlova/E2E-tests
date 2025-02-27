import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChrOpt
from selenium.webdriver.firefox.options import Options as FireOpt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
import logging
logging.basicConfig(encoding='utf-8')



@pytest.fixture(scope="class")
def driver(pytestconfig):
    options = ChrOpt()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")

    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

