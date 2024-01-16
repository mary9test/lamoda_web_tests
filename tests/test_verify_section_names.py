from lamoda_test_framework.pages import main_page
import allure


@allure.title("Соответствие названий разделов")
@allure.tag("web_tests")
@allure.feature("main_page")
@allure.severity('critical')
def test_verify_section_names():
    main_page.open_browser()
    main_page.verify_menu_item_text('женщин', "Женщинам")
    main_page.verify_menu_item_text('мужчин', "Мужчинам")
    main_page.verify_menu_item_text('детей', "Детям")
