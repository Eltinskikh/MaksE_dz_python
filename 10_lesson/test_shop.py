import allure
from selenium import webdriver
from pages.shop_page import LoginPage, InventoryPage, CartPage, CheckoutPage


@allure.feature("Online Shop")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("Проверка процесса покупки товаров и итоговой суммы")
def test_saucedemo():
    driver = webdriver.Chrome()
    try:
        login_page = LoginPage(driver)

        with allure.step("Открытие страницы авторизации"):
            login_page.open()

        with allure.step("Вход в систему"):
            login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        with allure.step("Добавление товаров в корзину"):
            for item in items_to_add:
                with allure.step(f"Добавление {item}"):
                    inventory_page.add_item_to_cart(item)

        with allure.step("Переход в корзину"):
            inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        with allure.step("Начало оформления заказа"):
            cart_page.checkout()

        checkout_page = CheckoutPage(driver)
        with allure.step("Заполнение информации о доставке"):
            checkout_page.fill_shipping_info("Иван", "Иванов", "123456")

        with allure.step("Переход к обзору заказа"):
            checkout_page.continue_to_overview()

        with ((((allure.step("Проверка итоговой суммы"))))):
            total_amount = checkout_page.get_total_amount()
            assert total_amount == "58.29", (f"Ожидалось: $58.29, Получено: "
                                             f"${total_amount}")

    finally:
        driver.quit()
