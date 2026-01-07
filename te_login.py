import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_valid_login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By,ID, "login").send_key("SuperSecretlogin!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "You logged into a secure area!" in driver.page_source
    driver.quit()
