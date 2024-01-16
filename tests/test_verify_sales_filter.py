from lamoda_test_framework.pages import main_page, sale_page
import allure


@allure.title("Названия фильтра на странице Sale")
@allure.tag("web_tests")
@allure.feature("resale_page")
@allure.severity('critical')
def test_verify_resale_text():
    main_page.open_browser()
    main_page.go_to_sale_page()
    sale_page.verify_filter_names_sale()
