from Page_en.home_page import HomePage
from Page_en.login_page import LoginPage
from Page_en.pay_page import PayPage
from Page_en.premium_page import PremiumPage
from Page_en.test_page import Testpage


class Page:

    def __init__(self,driver):
        self.driver = driver

    def get_home_page(self):
        """返回首页实例化对象"""
        return HomePage(self.driver)

    def get_login_page(self):
        """返回登录实例化对象"""
        return LoginPage(self.driver)

    def get_test_page(self):
        """返回测试权限页面实例化对象"""
        return Testpage(self.driver)

    def get_premium_page(self):
        """返回登录实例化对象"""
        return PremiumPage(self.driver)

    def get_pay_page(self):
        """返回支付页实例化对象"""
        return PayPage(self.driver)

