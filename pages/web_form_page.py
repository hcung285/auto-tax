from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WebFormPage(BasePage):
    """Selenium's public demo form: https://www.selenium.dev/selenium/web/web-form.html"""

    path = "web-form.html"

    TEXT_INPUT = (By.ID, "my-text-id")
    PASSWORD_INPUT = (By.NAME, "my-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    MESSAGE = (By.ID, "message")

    def fill_text(self, text: str):
        self.type(self.TEXT_INPUT, text)
        return self

    def submit(self) -> str:
        self.click(self.SUBMIT_BUTTON)
        return self.text_of(self.MESSAGE)
