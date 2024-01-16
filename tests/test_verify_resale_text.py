from lamoda_test_framework.pages import resale_page
from lamoda_test_framework.pages import main_page
import allure


@allure.title("Соотвествие текста на странице Resale")
@allure.tag("web_tests")
@allure.feature("resale_page")
@allure.severity('critical')
def test_verify_resale_text():
    main_page.open_browser()
    main_page.go_to_resale_page()
    resale_page.click_about_button()
    resale_page.verify_text_about_resale()
