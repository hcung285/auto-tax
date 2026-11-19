import pytest

from config import settings
from pages.login_page import LoginPage


@pytest.fixture
def credentials():
    if not settings.ETAX_USERNAME or not settings.ETAX_PASSWORD:
        pytest.skip("Set ETAX_USERNAME and ETAX_PASSWORD in .env to run eTax tests")
    return settings.ETAX_USERNAME, settings.ETAX_PASSWORD


@pytest.mark.smoke
def test_open_create_taxpayer_account(credentials, driver, base_url):
    username, password = credentials

    # Step 1-2: open the browser and go to <BASE_URL>/Request
    login_page = LoginPage(driver, base_url).open()

    # Step 3: log in
    home_page = login_page.login(username, password)

    # Step 4: Quản lý NNT -> Tạo tài khoản NNT
    home_page.open_quan_ly_nnt_menu()
    home_page.open_tao_tai_khoan_nnt()

    url = home_page.wait_for_create_account_form()
    assert "dse_operationName=adminCreateAccountRetail" in url
