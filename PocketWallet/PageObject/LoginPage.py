import time
from macaca import WebDriverException

from Public.BasePage import BasePage
from Public.Decorator import teststep
from Public.Decorator import teststeps

# from App.PageObject.GesturePasswordPage import GesturePasswordPage
# from Public.LoginStatus import LoginStatus
from PocketWallet.PageObject.PocketWalletHomePage import PocketWalletHomePage
from PocketWallet.TestData.Account import VALID_ACCOUNT


class LoginPage(BasePage):
    @teststep
    def wait_page(self, timeout=10000):
        """以登录页面的“登录”Button的ID为依据"""
        try:
            self.driver\
                .wait_for_element_by_xpath('/html/body/div[1]/div/form/button', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def back(self):
        self.driver.element_by_id('cn.pocketwallet.pocketwallet:id/iv_nav_back').click()

    @teststep
    def input_account(self, account):
        """以“请输入手机号码”的xpath为依据"""
        self.driver\
            .element_by_xpath('/html/body/div[1]/div/form/div[1]/p/input')\
            .clear()\
            .send_keys(account)

    @teststep
    def input_password(self, pwd):
        """以“请输入登录密码”的XPATH为依据"""
        self.driver\
            .element_by_xpath('/html/body/div[1]/div/form/p/input')\
            .clear()\
            .send_keys(pwd)

    @teststep
    def login(self):
        """以“登录”Button的xpath为依据"""
        self.driver\
            .element_by_xpath('/html/body/div[1]/div/form/button')\
            .click()

    @teststep
    def switch_webview(self):
        """切换到webview，操作H5"""
        contexts = self.driver.contexts
        self.driver.context = contexts[-1]

    @teststep
    def switch_native(self):
        """切换到native"""
        contexts = self.driver.contexts
        self.driver.context = contexts[0]

    @teststeps
    def new_valid_login(self):
        """用给定的account与password进行登录"""
        login = LoginPage()
        login.switch_webview()
        login.input_account(VALID_ACCOUNT.account())
        login.input_password(VALID_ACCOUNT.password())
        login.login()
        time.sleep(1)
        login.switch_native()




