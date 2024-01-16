from lamoda_test_framework.pages import main_page
import allure


@allure.title("Результаты поиска соответствуют запросу")
@allure.tag("web_tests")
@allure.feature("search_page")
@allure.severity('critical')
def test_search():
    input_request_value = "брюки"
    main_page.open_browser()
    main_page.search_for_item(input_request=input_request_value)
    main_page.verify_search(input_request=input_request_value)
