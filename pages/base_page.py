from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings

Locator = tuple[str, str]


class BasePage:
    path = ""

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, settings.EXPLICIT_WAIT)

    def open(self):
        self.driver.get(f"{self.base_url}/{self.path.lstrip('/')}")
        return self

    @property
    def title(self) -> str:
        return self.driver.title

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: Locator, text: str) -> None:
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator: Locator) -> str:
        return self.find(locator).text
