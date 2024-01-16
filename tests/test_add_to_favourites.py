from lamoda_test_framework.pages import brands_page
import allure


@allure.title("Добавление бренда в Избранное")
@allure.tag("web_tests")
@allure.feature("brands_page")
@allure.severity('critical')
def test_add_to_favourites():
    brands_page.open_browser()
    brands_page.go_to_brands_page()
    brands_page.add_brand_to_favourites()
    brands_page.go_to_favourites_brands()
    brands_page.verify_favourite_brand_name()
