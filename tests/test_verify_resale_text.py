from lamoda_test_framework.pages.resale_page import resale
from lamoda_test_framework.pages.main_page import main
import allure


@allure.title("Соотвествие текста на странице Resale")
@allure.tag("web_tests")
@allure.feature("resale_page")
@allure.severity('critical')
def test_verify_resale_text():
    main.open_browser()
    main.go_to_resale_page()
    resale.click_about_button()
    resale.verify_text_about_resale()
