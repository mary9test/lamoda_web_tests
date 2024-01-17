from lamoda_test_framework.pages.main_page import main
from lamoda_test_framework.pages.sale_page import sale
import allure


@allure.title("Названия фильтра на странице Sale")
@allure.tag("web_tests")
@allure.feature("resale_page")
@allure.severity('critical')
def test_verify_resale_text():
    main.open_browser()
    main.go_to_sale_page()
    sale.verify_filter_names_sale()
