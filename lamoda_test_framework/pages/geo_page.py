from selene import browser, have
import allure


class GeoPage:
    def open_browser(self):
        with allure.step("Открываем браузер"):
            browser.open("/women-home/")

    def geo_click(self):
        with allure.step("Нажимаем выбор местоположения"):
            browser.element('div[class*="js-header-geo-wrapper"]').click()

    def select_city(self):
        with allure.step("Выбираем город"):
            browser.element('div[class*="citiesList"] > :first-child').click()

    def select_city_verify_result(self):
        with allure.step("Проверяем успешный выбор местоположения"):
            browser.element('div[class*="locationTitle"]').should(have.text("Вы находитесь в г. Москва"))


geolocation = GeoPage()
