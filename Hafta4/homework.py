from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Sauce:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(3)

    def test_empty_login(self):
        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.click()
        sleep(2)

        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(testResult)
        print(f"Test Result: {testResult}")

    def test_emptyPassword_login(self):
        usernameInput = self.driver.find_element(By.ID, 'user-name')
        usernameInput.send_keys('Hi')
        sleep(2)

        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.click()
        sleep(2)

        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(testResult)
        print(f"Test Result: {testResult}")

    def test_invalid_login(self):
        username = 'locked_out_user'
        password = 'secret_sauce'

        usernameInput = self.driver.find_element(By.ID, 'user-name')
        passwordInput = self.driver.find_element(By.ID, 'password')

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        sleep(2)


        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.send_keys(Keys.ENTER)
        sleep(3)

        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

        testResult = errorMessage.text == 'Epic sadface: Sorry, this user has been locked out.'
        print(testResult)
        print(f"Test Result = {testResult}")

    def test_icon_login(self):
        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.send_keys(Keys.ENTER)
        sleep(3)

        errorIcons = self.driver.find_elements(By.CLASS_NAME, 'error_icon')
        sleep(3)

        errorBtn = self.driver.find_element(By.CLASS_NAME, 'error-button')
        errorBtn.click()

    def test_success_login(self):
        username1 = 'standard_user'
        password1 = 'secret_sauce'

        usernameInput = self.driver.find_element(By.ID, 'user-name')
        passwordInput = self.driver.find_element(By.ID, 'password')

        usernameInput.send_keys(username1)
        passwordInput.send_keys(password1)
        sleep(2)

        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.send_keys(Keys.ENTER)
        sleep(3)

        inventoryItem = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')

        print(f"Number of inventory items: {len(inventoryItem)}")
        
        sleep(100)

#? TEK TEK CALISTIRARAK TEST EDINIZ
testClass = Test_Sauce()
#testClass.test_empty_login()
#testClass.test_emptyPassword_login()
#testClass.test_invalid_login()
#testClass.test_icon_login()
#testClass.test_success_login()