from selenium.webdriver.common.by import By


class LoginPageLocators:

    username_textbox_name = "username"
    password_textbox_name = "password"
    login_button_xpath = '//button[@type="submit"]'
    google_search_editbox = "//textarea[@title='Search']"
    first_link_on_google_search = '//a[@href="https://opensource-demo.orangehrmlive.com/"]'
    url = "https://www.google.com/"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
