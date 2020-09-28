import Page_en
from Base_en.base import Base
from time import sleep


class PremiumPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_login(self):
        self.click_element(Page_en.premium_login_xpath)

    def click_3_months(self):
        # 点击3个月套餐
        self.click_element(Page_en.premium_3_months_xpath)
        sleep(1)

    def click_6_months(self):
        # 点击6个月套餐
        self.click_element(Page_en.premium_6_months_xpath)
        sleep(1)

    def click_annual(self):
        # 点击年套餐
        self.click_element(Page_en.premium_annual_xpath)
        sleep(1)

    def click_lifetime(self):
        # 点击终身套餐
        self.click_element(Page_en.premium_lifetime_xpath)
        sleep(1)

    def click_ok(self):
        # 支付成功跳会员，当前为第2个页面并切换
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(2)
        # 点击支付成功ok按钮跳回首页
        self.click_element(Page_en.premium_pay_success_ok_xpath)
        sleep(3)

