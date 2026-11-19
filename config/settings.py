import os

from dotenv import load_dotenv

load_dotenv()


def _bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


# Application under test
BASE_URL = os.getenv("BASE_URL", "https://thuedientu.tct.vn/etaxcbt").rstrip("/")

# Login credentials - keep them in .env (git-ignored), never in source code
ETAX_USERNAME = os.getenv("ETAX_USERNAME", "")
ETAX_PASSWORD = os.getenv("ETAX_PASSWORD", "")

# Browser
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = _bool(os.getenv("HEADLESS", "false"))
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "0"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
