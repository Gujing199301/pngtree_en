import os,sys
sys.path.append(os.getcwd())
from Base_en.page import Page
from Base_en.initdriver import get_driver
from time import sleep
import pytest


class TestLogin:

    def setup_class(self):
        # 引入driver
        self.driver = get_driver()
        sleep(1)
        self.driver.get('https://pngtree.com/')
        # 窗口最大化
        self.driver.maximize_window()
        # 创建页面统一入口类方便调用页面类
        self.page_obj = Page(self.driver)
        sleep(2)

    def setup(self):

        try:
            # 点击首页中的登录按钮
            self.page_obj.get_home_page().click_login()
            sleep(2)

        except:
            # 触发3次PV注册弹窗,刷新页面
            self.driver.refresh()
            sleep(2)
            # 再次点击首页中的登录按钮
            self.page_obj.get_home_page().click_login()
            sleep(2)

    def teardown(self):
        # 避免优惠券弹窗遮挡元素
        self.driver.refresh()
        sleep(3)
        # 退出登录
        self.page_obj.get_home_page().click_logout()
        sleep(3)

    def teardown_class(self):
        sleep(2)
        self.driver.quit()

    def test_email_login(self):
        # 邮箱登录
        self.page_obj.get_login_page().email_login('gujingqwertyuiop@gmail.com','1165509917@qq.com')

    def test_fb_login(self):
        # fb登录
        self.page_obj.get_login_page().fb_login('2505312014@qq.com','pngtree2020')

    def test_twitter_login(self):
        self.page_obj.get_login_page().twitter_login('1280365716@qq.com','gujing199301')


if __name__ == '__main__':
    pytest.main(['-s','-q','test_login.py'])
