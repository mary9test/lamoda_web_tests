from selene import browser, have
import allure


def open_browser():
    browser.open("/women-home/")


def get_menu_item(gender):
    with allure.step("Получаем название раздела"):
        return browser.element(f'[aria-label="Товары для {gender}"]')


def go_to_kids_page():
    with allure.step("Переходим в раздел дети"):
        browser.element('[data-genders="kids"]').click()


def go_to_resale_page():
    with allure.step("Переходим в раздел Resale"):
        browser.element('[aria-label="Главное меню"] > :nth-child(9)').click()


def verify_menu_item_text(gender, expected_text):
    with allure.step("Проверяем что название раздела соотвествует ожидаемому"):
        get_menu_item(gender).should(have.text(expected_text))


def search_for_item(input_request):
    with allure.step("Выполняем поиск по сайту"):
        search_input = browser.element('input[class*="_input_"]')
        search_input.click().type(input_request).press_enter()


def verify_search(input_request):
    with allure.step("Проверяем результат поиска"):
        browser.element('h2[class*="catalog-search-head-title"]').should(
            have.text(f"Товары по запросу «{input_request}»"))
