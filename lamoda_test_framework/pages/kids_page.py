from selene import browser, have
import allure


class KidsSectionPage:
    def open_browser(self):
        with allure.step("Открываем браузер"):
            browser.open("/women-home/")

    def select_school_section(self):
        with allure.step("Переходим в раздел игрушки"):
            browser.element('nav [href*="detskieigrushki"]').click()

    def verify_filter_names(self):
        with allure.step("Проверяем названия фильтров в разделе игрушки"):
            browser.element('[class *="filters-widget"]>:nth-child(6)').should(have.text('Back to school'))
            browser.element('[class *="filters-widget"]>:nth-child(7)').should(have.text('Возраст детей'))


kids = KidsSectionPage()
