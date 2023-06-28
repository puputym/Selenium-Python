import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def test_a_success_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

    def test_a_failed_login_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > h3").text
        self.assertIn('Epic sadface: Username is required', response_data)

    def test_a_failed_login_with_empty_passwrod(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > h3").text
        self.assertIn('Epic sadface: Password is required', response_data)
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()