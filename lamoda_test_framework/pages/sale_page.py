from selene import browser, have
import allure


def verify_filter_names_sale():
    with allure.step("Проверяем названия фильтров в разделе Sale"):
        browser.element('[class *="filters-widget"]>:nth-child(8)').should(have.text('Только со скидкой'))
