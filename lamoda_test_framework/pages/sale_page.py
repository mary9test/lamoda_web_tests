from selene import browser, have
import allure


class SalePage:

    def verify_filter_names_sale(self):
        with allure.step("Проверяем названия фильтров в разделе Sale"):
            browser.element('[class *="filters-widget"]>:nth-child(8)').should(have.text('Только со скидкой'))


sale = SalePage()
