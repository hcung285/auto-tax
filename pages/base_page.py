from selenium.common.exceptions import (
    NoSuchFrameException,
    StaleElementReferenceException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings

Locator = tuple[str, str]

FRAMES = (By.CSS_SELECTOR, "frame, iframe")
MAX_FRAME_DEPTH = 3


class BasePage:
    path = ""

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(
            driver,
            settings.EXPLICIT_WAIT,
            ignored_exceptions=(StaleElementReferenceException, NoSuchFrameException),
        )

    def open(self):
        self.driver.get(f"{self.base_url}/{self.path.lstrip('/')}")
        return self

    @property
    def title(self) -> str:
        return self.driver.title

    # --- elements in the current document -------------------------------
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

    # --- elements that may live inside (nested) frames -------------------
    def find_in_any_frame(self, locator: Locator) -> WebElement:
        """Wait for a visible element in the page or any nested frame.

        Leaves the driver switched into the frame that holds the element.
        """

        def _search(driver: WebDriver):
            driver.switch_to.default_content()
            return self._search_frames(locator, depth=0)

        return self.wait.until(_search, message=f"Element not found in any frame: {locator}")

    def click_in_any_frame(self, locator: Locator) -> None:
        element = self.find_in_any_frame(locator)
        try:
            element.click()
        except WebDriverException:
            # Legacy menus sometimes sit under overlays; fall back to a JS click.
            self.driver.execute_script("arguments[0].click();", element)

    def switch_to_frame_named(self, name: str) -> None:
        """Switch into a frame by name/id, wherever it is nested."""
        frame = self.find_in_any_frame((By.CSS_SELECTOR, f"frame[name='{name}'], iframe[name='{name}'], #{name}"))
        self.driver.switch_to.frame(frame)

    def _search_frames(self, locator: Locator, depth: int):
        for element in self.driver.find_elements(*locator):
            if element.is_displayed():
                return element
        if depth >= MAX_FRAME_DEPTH:
            return None
        for frame in self.driver.find_elements(*FRAMES):
            self.driver.switch_to.frame(frame)
            found = self._search_frames(locator, depth + 1)
            if found is not None:
                return found
            self.driver.switch_to.parent_frame()
        return None
