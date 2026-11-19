import pytest

from pages.web_form_page import WebFormPage


@pytest.mark.smoke
def test_page_title(driver, base_url):
    page = WebFormPage(driver, base_url).open()
    assert page.title == "Web form"


@pytest.mark.regression
def test_submit_form(driver, base_url):
    page = WebFormPage(driver, base_url).open()
    message = page.fill_text("Hello Selenium").submit()
    assert message == "Received!"
