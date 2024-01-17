from lamoda_test_framework.pages.gifts_card_page import gift_card
from lamoda_test_framework.pages.main_page import main
import allure


@allure.title("Соответствие заголовка подарочной карты")
@allure.tag("web_tests")
@allure.feature("gift_card_page")
@allure.severity('critical')
def test_gift_card_amount_title():
    main.open_browser()
    main.search_for_item("подарочный сертификат")
    gift_card.verify_card_amount_title()


@allure.title("Доступные суммы для подарочных карт")
@allure.tag("web_tests")
@allure.feature("gift_card_page")
@allure.severity('critical')
def test_gift_card_amount():
    main.open_browser()
    main.search_for_item("подарочный сертификат")
    gift_card.verify_card_amount()
