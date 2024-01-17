from lamoda_test_framework.pages.main_page import main
from lamoda_test_framework.pages.kids_page import kids
import allure


@allure.title("Названия фильтров в разделе Дети")
@allure.tag("web_tests")
@allure.feature("kids_page")
@allure.severity('critical')
def test_kids_page():
    main.open_browser()
    main.go_to_kids_page()
    kids.select_school_section()
    kids.verify_filter_names()
