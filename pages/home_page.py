from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    """eTax CBT main screen shown after login (horizontal top menu)."""

    CONTENT_FRAME = "rframe"
    CREATE_ACCOUNT_OPERATION = "adminCreateAccountRetail"

    # <div class="text_memu_ngang">Quản lý NNT</div>  (CSS uppercases it; DOM text is as written)
    MENU_QUAN_LY_NNT = (
        By.XPATH,
        "//div[contains(@class, 'text_memu_ngang') and normalize-space(.)='Quản lý NNT']",
    )
    # <a href="...dse_operationName=adminCreateAccountRetail..." target="rframe">Tạo tài khoản NNT</a>
    # dse_sessionId changes per login, so match on the operation name only.
    LINK_TAO_TAI_KHOAN_NNT = (
        By.XPATH,
        f"//a[contains(@href, 'dse_operationName={CREATE_ACCOUNT_OPERATION}')]",
    )

    def open_quan_ly_nnt_menu(self) -> "HomePage":
        self.click_in_any_frame(self.MENU_QUAN_LY_NNT)
        return self

    def open_tao_tai_khoan_nnt(self) -> "HomePage":
        self.click_in_any_frame(self.LINK_TAO_TAI_KHOAN_NNT)
        return self

    def content_frame_url(self) -> str:
        """URL currently loaded in the content frame (rframe)."""
        self.driver.switch_to.default_content()
        self.switch_to_frame_named(self.CONTENT_FRAME)
        url = self.driver.execute_script("return window.location.href;")
        self.driver.switch_to.default_content()
        return url

    def wait_for_create_account_form(self) -> str:
        """Wait until rframe has loaded the 'Tạo tài khoản NNT' screen; return its URL."""
        def _loaded(_):
            url = self.content_frame_url()
            return url if self.CREATE_ACCOUNT_OPERATION in url else False

        return self.wait.until(_loaded, message="'Tạo tài khoản NNT' screen did not load in rframe")
