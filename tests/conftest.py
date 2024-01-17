import os

import pytest
from dotenv import load_dotenv

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lamoda_test_framework.utils import attach


def pytest_addoption(parser):
    parser.addoption('--remote_url', default='')


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def init_browser(request):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
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
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
