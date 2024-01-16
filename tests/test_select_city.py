from lamoda_test_framework.pages import geo_page
import allure


@allure.title("Выбор местоположения юзером")
@allure.tag("web_tests")
@allure.feature("geo_page")
@allure.severity('critical')
def test_select_city():
    geo_page.open_browser()
    geo_page.geo_click()
    geo_page.select_city()
    geo_page.select_city_verify_result()
