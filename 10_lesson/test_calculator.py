import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage, ResultPage


@allure.feature("Calculator")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест работы калькулятора")
@allure.description("Проверка вычисления 7 + 8 = 15 с заданной задержкой")
def test_calculator():
    driver = webdriver.Chrome()
    try:
        calculator_page = CalculatorPage(driver)

        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки в 45 секунд"):
            calculator_page.set_delay("45")

        with allure.step("Ввод выражения 7 + 8 ="):
            calculator_page.click_buttons("7", "+", "8", "=")

        result_page = ResultPage(driver)
        with allure.step("Ожидание результата"):
            result_page.wait_for_result(45)

        with allure.step("Проверка результата"):
            result_text = result_page.get_result()
            assert result_text == "15", f"Ожидалось 15, получено {result_text}"

    finally:
        driver.quit()
