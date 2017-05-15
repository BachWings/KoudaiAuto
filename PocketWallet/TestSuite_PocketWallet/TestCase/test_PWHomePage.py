__author__ = 'Bach'

import unittest
import time

# from Public.Drivers import Drivers
from Public.Decorator import setupclass
from Public.Decorator import teardownclass
from Public.Decorator import setup
from Public.Decorator import teardown
from Public.Decorator import testcase

from PocketWallet.PageObject.PocketWalletHomePage import PocketWalletHomePage
from PocketWallet.PageObject.LoginPage import LoginPage


# from App.PageObject.PlatformAppHomePage import back_to_app
# from PocketWallet.PageObject.WizardPage import WizardPage


class PWHomePage(unittest.TestCase):
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.home_page = PocketWalletHomePage()

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        pass

    @setup
    def setUp(self):
        pass
        # back_to_app()

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_HomePage_001_Open(self):
        """确认打开首页"""
        self.assertFalse(self.home_page.wait_page())

    @testcase
    def test_HomePage_002_Login(self):
        """首页登录功能检查"""
        self.home_page.click_usr_account()
        login_page = LoginPage()
        login_page.new_valid_login()
        self.assertTrue(self.home_page.is_login())
