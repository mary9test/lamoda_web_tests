from lamoda_test_framework.pages.main_page import main
import allure


@allure.title("Соответствие названий разделов")
@allure.tag("web_tests")
@allure.feature("main_page")
@allure.severity('critical')
def test_verify_section_names():
    main.open_browser()
    main.verify_menu_item_text('женщин', "Женщинам")
    main.verify_menu_item_text('мужчин', "Мужчинам")
    main.verify_menu_item_text('детей', "Детям")
