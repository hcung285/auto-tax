import os

from dotenv import load_dotenv

load_dotenv()


def _bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


BASE_URL = os.getenv("BASE_URL", "https://www.selenium.dev/selenium/web").rstrip("/")
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = _bool(os.getenv("HEADLESS", "true"))
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "0"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))
