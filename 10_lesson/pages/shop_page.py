from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def checkout(self) -> None:
    """Начинает процесс оформления заказа"""
    wait = WebDriverWait(self.driver, 10)
    checkout_button = (wait.until
                       (EC.element_to_be_clickable((By.ID, "checkout"))))
    checkout_button.click()


class LoginPage:
    """Класс для работы со страницей авторизации"""
    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """Выполняет вход в систему
        Args:
            username: имя пользователя
            password: пароль
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    """Класс для работы со страницей каталога товаров"""
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name: str) -> None:
        """Добавляет товар в корзину
        Args:
            item_name: название товара
        """
        item_xpath = (f"//div[text()='{item_name}']/ancestor:"
                      f":div[@class='inventory_item']//button")
        self.driver.find_element(By.XPATH, item_xpath).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    """Класс для работы со страницей корзины"""
    def __init__(self, driver):
        self.driver = driver

    def checkout(self) -> None:
        """Начинает процесс оформления заказа"""
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    """Класс для работы со страницей оформления заказа"""
    def __init__(self, driver):
        self.driver = driver

    def fill_shipping_info(self, first_name: str,
                           last_name: str, postal_code: str) -> None:
        """Заполняет информацию о доставке
        Args:
            first_name: имя
            last_name: фамилия
            postal_code: почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_to_overview(self) -> None:
        """Переходит к обзору заказа"""
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self) -> str:
        """Получает итоговую сумму заказа
        Returns:
            str: сумма в формате строки без символа $
        """
        return (
            self.driver.find_element(By.CLASS_NAME, "summary_total_label")
            .text.split("$")[1]
        )
