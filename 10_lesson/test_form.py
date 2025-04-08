import allure
from selenium import webdriver
from pages.form_page import FormPage, ResultPage


@allure.feature("Form Submission")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест заполнения формы")
@allure.description("Проверка корректности обработки формы без ZIP code")
def test_form_submission():
    driver = webdriver.Chrome()
    try:
        form_page = FormPage(driver)

        with allure.step("Открытие страницы формы"):
            form_page.open()

        with allure.step("Заполнение полей формы"):
            form_page.fill_first_name("Иван")
            form_page.fill_last_name("Петров")
            form_page.fill_address("Ленина, 55-3")
            form_page.fill_email("test@skypro.com")
            form_page.fill_phone("+7985899998787")
            form_page.fill_city("Москва")
            form_page.fill_country("Россия")
            form_page.fill_job_position("QA")
            form_page.fill_company("SkyPro")

        with allure.step("Отправка формы"):
            form_page.submit()

        result_page = ResultPage(driver)
        with allure.step("Ожидание результатов"):
            result_page.wait_for_zip_code_highlight()

        with (((allure.step("Проверка подсветки поля ZIP code красным")))):
            error_message = "Поле ZIP code не подсвечено красным"
            assert result_page.is_zip_code_highlighted_red(), error_message

        fields_to_check = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]
        for field in fields_to_check:
            with allure.step(f"Проверка подсветки поля {field} зеленым"):
                assert result_page.is_field_highlighted_green(field), \
                    f"Поле {field} не подсвечено зеленым"

    finally:
        driver.quit()
