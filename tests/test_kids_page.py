from lamoda_test_framework.pages import kids_page, main_page
import allure


@allure.title("Названия фильтров в разделе Дети")
@allure.tag("web_tests")
@allure.feature("kids_page")
@allure.severity('critical')
def test_kids_page():
    main_page.open_browser()
    main_page.go_to_kids_page()
    kids_page.select_school_section()
    kids_page.verify_filter_names()
