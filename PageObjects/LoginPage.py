from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_xpath = "//a[@href='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, textbox_username_id).clear()
        self.driver.find_element(By.ID, textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, textbox_password_id).clear()
        self.driver.find_element(By.ID, textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, link_logout_xpath).click()
