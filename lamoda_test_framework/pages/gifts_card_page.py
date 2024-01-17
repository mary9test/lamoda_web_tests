from selene import browser, have
import allure


class GiftCard:

    def open_browser(self):
        with allure.step("Открываем браузер"):
            browser.open("/women-home/")

    def verify_card_amount_title(self):
        with allure.step("Проверяем заголовок выбора стоимости карты"):
            browser.element('[class *="amountTitle"]').should(have.text('Сколько хотите подарить'))

    def verify_card_amount(self):
        with allure.step("Проверяем на какую сумму можно выбрать подарочную карту"):
            browser.element('[class*=amountItem]:first-of-type').should(have.text('5 000 ₽'))
            browser.element('[class*=amountItem]:nth-of-type(2)').should(have.text('10 000 ₽'))
            browser.element('[class*=amountItem]:nth-of-type(3)').should(have.text('15 000 ₽'))
            browser.element('[class*=amountItem]:nth-of-type(4)').should(have.text('20 000 ₽'))
            browser.element('[class*=amountItem]:nth-of-type(5)').should(have.text('Другая сумма'))


gift_card = GiftCard()
