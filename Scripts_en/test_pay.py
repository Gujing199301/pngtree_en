import os,sys
sys.path.append(os.getcwd())
from Base_en.initdriver import get_driver
from Base_en.page import Page
from time import sleep
import pytest


class TestPay:

    def setup(self):
        self.driver = get_driver()
        sleep(3)
        self.driver.get('https://pngtree.com/pay?b=1')
        self.driver.maximize_window()
        self.page_obj = Page(self.driver)
        sleep(3)

        # 在会员页登录
        self.page_obj.get_premium_page().click_login_premium()
        sleep(2)
        self.page_obj.get_login_page().email_login('gujing199301@163.com', '1165509917@qq.com')
        sleep(2)
        # 新窗口打开测试权限
        js = 'window.open("https://pngtree.com/test?pass=zxcvb")'
        self.driver.execute_script(js)
        sleep(1)

        # 切换至测试权限窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])

        # 操作1-刷新pv
        self.page_obj.get_test_page().flush_pv()

        # 操作2-点击清除vip
        self.page_obj.get_test_page().clear_vip()

        # 操作3-变成第一次登录
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/a').click()

        # 关闭当前窗口
        self.driver.close()
        # 切换至原来的窗口
        self.driver.switch_to.window(f[0])
        self.driver.refresh()
        sleep(3)
        self.driver.refresh()
        sleep(3)

    def teardown(self):

        # 切换为会员页，此时是第二个页面
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])

        # 点击支付成功弹窗ok按钮跳回首页
        self.page_obj.get_premium_page().click_ok()
        sleep(1)

        # 截图
        self.page_obj.get_home_page().screen_user_vip()
        sleep(2)
        self.driver.quit()

    def test_card(self):

        # 在会员页点击季度套餐
        self.page_obj.get_premium_page().click_3_months()
        sleep(1)

        # 使用钱海充值季套餐
        self.page_obj.get_pay_page().card_pay()

    # def test_paypal(self):
    #
    #     # 在会员页点击6个月套餐
    #     self.page_obj.get_premium_page().click_6_months()
    #     sleep(1)
    #
    #     # 使用paypal充值6个月套餐
    #     self.page_obj.get_pay_page().paypal_pay()
    #
    # def test_pw(self):
    #     # 在会员页点击终身套餐
    #     self.page_obj.get_premium_page().click_lifetime()
    #     sleep(1)
    #
    #     # 选择本地方式充值终身套餐
    #     self.page_obj.get_pay_page().pw_pay()
    #
    # def test_palpal_card(self):
    #     # 在会员页点击1年套餐
    #     self.page_obj.get_premium_page().click_annual()
    #     sleep(1)
    #
    #     # 使用paypal信用卡充值1年套餐
    #     self.page_obj.get_pay_page().paypal_card_pay()
    #







if __name__ == '__main__':
    pytest.main(['-s','-q','test_pay.py'])

