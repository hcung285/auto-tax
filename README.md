# auto-tax

Python UI automation tests with Selenium 4 and pytest (Page Object Model) for the eTax CBT portal
(`https://thuedientu.tct.vn/etaxcbt`).

## Scenario covered

`tests/test_create_taxpayer_account.py`

1. Open the browser
2. Go to `<BASE_URL>/Request`
3. Log in with `ETAX_USERNAME` / `ETAX_PASSWORD` (fields `#_userName`, `#password`)
4. Click the top menu **Quản lý NNT**, then **Tạo tài khoản NNT**, and check the screen loads in `rframe`

## Structure

```
config/settings.py        # env-driven settings (BASE_URL, BROWSER, HEADLESS, waits)
utils/driver_factory.py   # creates Chrome / Firefox / Edge drivers
pages/                    # page objects: BasePage (frame-aware helpers), LoginPage, HomePage
tests/                    # test cases
conftest.py               # fixtures, CLI options, screenshot on failure
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (source .venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
cp .env.example .env          # then fill in ETAX_USERNAME / ETAX_PASSWORD
```

Credentials live only in `.env`, which is git-ignored. Without them the eTax tests are skipped.

Selenium Manager downloads the matching browser driver automatically.

## Run

```bash
pytest                         # all tests in Chrome (HEADLESS=true in .env to hide the window)
pytest -m smoke                # only smoke tests
pytest --browser firefox       # another browser
pytest --headed                # show the browser window
pytest -n 4                    # parallel (pytest-xdist)
```

An HTML report is written to `reports/report.html`; failed tests save screenshots to `screenshots/`.
