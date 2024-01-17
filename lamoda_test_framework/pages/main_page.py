from selene import browser, have
import allure


class MainPage:
    def open_browser(self):
        with allure.step("Открываем браузер"):
            browser.open("/women-home/")

    def get_menu_item(self, gender):
        with allure.step("Получаем название раздела"):
            return browser.element(f'[aria-label="Товары для {gender}"]')

    def go_to_kids_page(self):
        with allure.step("Переходим в раздел дети"):
            browser.element('[data-genders="kids"]').click()

    def go_to_resale_page(self):
        with allure.step("Переходим в раздел Resale"):
            browser.element('[aria-label="Главное меню"] > :nth-child(9)').click()

    def go_to_sale_page(self):
        with allure.step("Переходим в раздел Sale"):
            browser.element('[aria-label="Главное меню"] > :nth-child(12)').click()

    def verify_menu_item_text(self, gender, expected_text):
        with allure.step("Проверяем что название раздела соотвествует ожидаемому"):
            self.get_menu_item(gender).should(have.text(expected_text))

    def search_for_item(self, input_request):
        with allure.step("Выполняем поиск по сайту"):
            search_input = browser.element('input[class*="_input_"]')
            search_input.click().type(input_request).press_enter()

    def verify_search(self, input_request):
        with allure.step("Проверяем результат поиска"):
            browser.element('h2[class*="catalog-search-head-title"]').should(
                have.text(f"Товары по запросу «{input_request}»"))


main = MainPage()
