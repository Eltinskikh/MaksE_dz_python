from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        (self.driver.get(
          "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        ))

    def set_delay(self, delay: str) -> None:
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text: str) -> None:
        (self.driver.find_element
         (By.XPATH, f"//span[text()='{button_text}']").click())

    def click_buttons(self, *buttons: str) -> None:
        for button in buttons:
            self.click_button(button)


class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_result(self, timeout: int) -> None:
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )

    def get_result(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
