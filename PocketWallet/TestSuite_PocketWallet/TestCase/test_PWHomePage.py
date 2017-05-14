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
    def test_PW_HomePage_Login(self):
        """首页"""
        self.home_page.click_usr_account()

        login_page = LoginPage()
        self.assertTrue(login_page.new_valid_login())