import os

import pytest
from dotenv import load_dotenv

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--remote_url', default='')


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def init_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    remote_url = request.config.getoption('--remote_url')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{remote_url}",
        options=options
    )

    browser.config.driver = driver

    browser.config.base_url = 'https://www.lamoda.ru'
    browser.config.window_width = 2880
    browser.config.window_height = 1800

    yield browser

    browser.quit()
