from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
for _ in range(5):
    add_button.click()
button_delete = driver.find_elements(By.XPATH, '//*[@id="elements"]/button')

print(len(button_delete))

sleep(5)

driver.quit()
