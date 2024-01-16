from selene import browser, have
import allure


def open_browser():
    browser.open("/women-home/")


def go_to_brands_page():
    with allure.step("Переходим на страницу брендов"):
        browser.element('[aria-label="Главное меню"] > :nth-child(6)').click()


def add_brand_to_favourites():
    with allure.step("Добавляем бренд в избранное"):
        browser.element('a[title="Mango"] .js-to-favorites').click()


def go_to_favourites_brands():
    with allure.step("Переходим в Любимые бренды"):
        browser.element('[href="/brands/?b=wishlist"]').click()


def verify_favourite_brand_name():
    with allure.step("Проверяем, что бренд был добавлен в категорию Любимые"):
        browser.element('.brands__link span').should(have.text('Mango'))
