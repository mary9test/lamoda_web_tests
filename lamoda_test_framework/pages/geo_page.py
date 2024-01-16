from selene import browser, have
import allure


def open_browser():
    browser.open("/women-home/")


def geo_click():
    with allure.step("Нажимаем выбор местоположения"):
        browser.element('div[class*="js-header-geo-wrapper"]').click()


def select_city():
    with allure.step("Выбираем город"):
        browser.element('div[class*="citiesList"] > :first-child').click()


def select_city_verify_result():
    with allure.step("Проверяем успешный выбор местоположения"):
        browser.element('div[class*="locationTitle"]').should(have.text("Вы находитесь в г. Москва"))
