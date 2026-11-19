from datetime import datetime
from pathlib import Path

import pytest

from config import settings
from utils.driver_factory import create_driver

SCREENSHOT_DIR = Path("screenshots")


def pytest_addoption(parser):
    parser.addoption("--browser", default=settings.BROWSER, help="chrome | firefox | edge")
    parser.addoption("--headed", action="store_true", help="Run with a visible browser window")
    parser.addoption("--base-url", default=settings.BASE_URL, help="Application base URL")


@pytest.fixture(scope="session")
def base_url(request) -> str:
    return request.config.getoption("--base-url").rstrip("/")


@pytest.fixture
def driver(request):
    headless = settings.HEADLESS and not request.config.getoption("--headed")
    drv = create_driver(request.config.getoption("--browser"), headless=headless)
    drv.implicitly_wait(settings.IMPLICIT_WAIT)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot when a test using the `driver` fixture fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv is not None:
            SCREENSHOT_DIR.mkdir(exist_ok=True)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            drv.save_screenshot(str(SCREENSHOT_DIR / f"{item.name}_{stamp}.png"))
