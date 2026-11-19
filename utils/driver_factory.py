from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def create_driver(browser: str = "chrome", headless: bool = True) -> WebDriver:
    """Create a WebDriver. Selenium Manager resolves the driver binary automatically."""
    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
        return driver

    if browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        return webdriver.Edge(options=options)

    raise ValueError(f"Unsupported browser: {browser}")
