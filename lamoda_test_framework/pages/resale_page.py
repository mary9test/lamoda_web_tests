from selene import browser, have
import allure


class ResalePage:

    def open_browser(self):
        with allure.step("Открываем браузер"):
            browser.open("/women-home/")

    def click_about_button(self):
        with allure.step("Нажимаем кнопку Подробнее"):
            browser.element('a[class*="aboutLink"]').click()

    def verify_text_about_resale(self):
        with allure.step("Проверяем текст на странице ресейла"):
            browser.element('div[class*="firstParagraph"]').should(have.text(
                "Ресейл — перепродажа новых или использованных вещей. Здесь вы найдете стильную одежду и аксессуары известных брендов, бывшие в употреблении."))


resale = ResalePage()
