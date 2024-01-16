from lamoda_test_framework.pages import gifts_card_page
from lamoda_test_framework.pages import main_page
import allure


@allure.title("Соответствие заголовка подарочной карты")
@allure.tag("web_tests")
@allure.feature("gift_card_page")
@allure.severity('critical')
def test_gift_card_amount_title():
    main_page.open_browser()
    main_page.search_for_item(input_request="подарочный сертификат")
    gifts_card_page.verify_card_amount_title()


@allure.title("Доступные суммы для подарочных карт")
@allure.tag("web_tests")
@allure.feature("gift_card_page")
@allure.severity('critical')
def test_gift_card_amount():
    main_page.open_browser()
    main_page.search_for_item(input_request="подарочный сертификат")
    gifts_card_page.verify_card_amount()
