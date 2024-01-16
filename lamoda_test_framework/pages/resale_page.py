from selene import browser, have
import allure


def open_browser():
    with allure.step("Открываем браузер"):
        browser.open("/women-home/")


def click_about_button():
    with allure.step("Нажимаем кнопку Подробнее"):
        browser.element('a[class*="aboutLink"]').click()


def verify_text_about_resale():
    with allure.step("Проверяем текст на странице ресейла"):
        browser.element('div[class*="firstParagraph"]').should(have.text(
            "Ресейл — перепродажа новых или использованных вещей. Здесь вы найдете стильную одежду и аксессуары известных брендов, бывшие в употреблении."))
