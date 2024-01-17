from lamoda_test_framework.pages.geo_page import geolocation
import allure


@allure.title("Выбор местоположения юзером")
@allure.tag("web_tests")
@allure.feature("geo_page")
@allure.severity('critical')
def test_select_city():
    geolocation.open_browser()
    geolocation.geo_click()
    geolocation.select_city()
    geolocation.select_city_verify_result()
