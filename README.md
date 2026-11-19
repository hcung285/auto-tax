# auto-tax

Python UI automation tests with Selenium 4 and pytest, using the Page Object Model.

## Structure

```
config/settings.py        # env-driven settings (BASE_URL, BROWSER, HEADLESS, waits)
utils/driver_factory.py   # creates Chrome / Firefox / Edge drivers
pages/                    # page objects (BasePage + one class per page)
tests/                    # test cases
conftest.py               # fixtures, CLI options, screenshot on failure
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (source .venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
cp .env.example .env          # optional
```

Selenium Manager downloads the matching browser driver automatically.

## Run

```bash
pytest                         # all tests, headless Chrome
pytest -m smoke                # only smoke tests
pytest --browser firefox       # another browser
pytest --headed                # show the browser window
pytest -n 4                    # parallel (pytest-xdist)
```

An HTML report is written to `reports/report.html`; failed tests save screenshots to `screenshots/`.
