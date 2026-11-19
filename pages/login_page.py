from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    """eTax CBT login screen: <BASE_URL>/Request"""

    path = "Request"

    USERNAME_INPUT = (By.ID, "_userName")
    PASSWORD_INPUT = (By.ID, "password")

    def login(self, username: str, password: str) -> HomePage:
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.find(self.PASSWORD_INPUT).send_keys(Keys.ENTER)
        return HomePage(self.driver, self.base_url)
