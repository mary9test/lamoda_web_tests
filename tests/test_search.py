from lamoda_test_framework.pages.main_page import main
import allure


@allure.title("Результаты поиска соответствуют запросу")
@allure.tag("web_tests")
@allure.feature("search_page")
@allure.severity('critical')
def test_search():
    main.open_browser()
    main.search_for_item("брюки")
    main.verify_search("брюки")
