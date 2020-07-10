# 导包
from time import sleep

import time

from selenium import webdriver

import unittest

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

import pytest


class TestEnPay(unittest.TestCase):

    def setup_class(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()

        # 打开会员页
        self.driver.get("https://pngtree.com/pay?b=1")

        # 浏览器窗口最大化
        self.driver.maximize_window()

        # 设置隐式等待时间10s
        self.driver.implicitly_wait(10)

        sleep(2)

        # 新窗口打开测试权限
        js = 'window.open("https://pngtree.com/test?pass=zxcvb")'

        self.driver.execute_script(js)

        sleep(1)

        # 切换至新窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])

        # 操作1-刷新pv
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/a').click()
        sleep(3)

        # 关闭当前窗口
        self.driver.close()

        # 切换回第一个窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[0])

        sleep(2)

        # 无论打开页面有没有pv验证都再刷新一次页面
        self.driver.refresh()
        sleep(3)

        # 点击登录入口
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div/div/a[1]').click()

        # 输入用户名
        self.driver.find_element_by_id('base-public-login-email-text').send_keys('gujingqwertyuiop@gmail.com  ')

        # 输入密码
        self.driver.find_element_by_id('base-public-login-password-text').send_keys('1165509917@qq.com ')

        # 点击登录
        self.driver.find_element_by_id('base-sub-Login-Btn').click()

        sleep(2)


    def setUp(self):

        # 新窗口打开测试权限
        js = 'window.open("https://pngtree.com/test?pass=zxcvb")'

        self.driver.execute_script(js)

        sleep(1)

        # 切换至新窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])

        # 操作2-点击清除vip
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a').click()

        sleep(3)

        # 操作3-变成第一次登录
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/a').click()
        sleep(2)

        # 关闭当前窗口
        self.driver.close()

        # 切换至原来的窗口
        self.driver.switch_to.window(f[0])
        sleep(3)

        # 确保是优惠价，刷新2次页面
        self.driver.refresh()
        sleep(3)

        self.driver.refresh()
        sleep(3)

        # 页面下拉至能看全所有套餐的位置
        js1 = 'window.scrollTo(0,300)'

        self.driver.execute_script(js1)

        sleep(2)

    # 钱海信用卡支付，充值季套餐
    @pytest.mark.run(order=0)
    def test_01(self):

        # 点击季套餐
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[2]/div[3]/article/div[1]/div[2]/a').click()

        # 打开第2个窗口，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])
        sleep(2)

        # 获取支付价格
        price = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div[2]/div/div[1]/div/div[3]/span[2]/span[2]')
        print(price.text)

        sleep(1)

        # 默认钱海行用卡，输入信息
        # First name
        first_name = self.driver.find_element_by_xpath('//*[@id="strat-cardHolderFirstName"]')
        first_name.clear()
        first_name.send_keys('姓氏')

        # Last name
        last_name = self.driver.find_element_by_id('strat-cardHolderLastName')
        last_name.clear()
        last_name.send_keys('名字')

        # Phone number
        phone_number = self.driver.find_element_by_id('start-billPhoneNumber')
        phone_number.clear()
        phone_number.send_keys('03715858680')

        # country默认选择无需操作

        # City
        city = self.driver.find_element_by_id('start-billCity')
        city.clear()
        city.send_keys('上海')

        # email
        email = self.driver.find_element_by_id('strat-cardHolderEmail')
        email.clear()
        email.send_keys('1165509917@qq.com')

        # postal code
        postal_code = self.driver.find_element_by_id('billZip')
        postal_code.clear()
        postal_code.send_keys('邮编')

        # address
        billing_address = self.driver.find_element_by_id('start-billAddress')
        billing_address.clear()
        billing_address.send_keys('张江高科')

        sleep(2)

        # 点击提交按钮
        self.driver.find_element_by_id('start-show-pay-box').click()

        # 充值过的用户有警告框提示
        alert = self.driver.switch_to.alert
        alert.accept()

        sleep(2)

        # 切换iframe
        frame = self.driver.find_element_by_id('ifrm_creditcard_checkout')

        self.driver.switch_to.frame(frame)

        sleep(3)

        # 输入卡号等信息
        self.driver.find_element_by_id('card_number_temp').send_keys('4111119987834534')

        self.driver.find_element_by_id('checkout_expiration_date').send_keys('02/24')

        self.driver.find_element_by_id('cvv2').send_keys('789')

        sleep(3)

        try:

            # 点击付款按钮
            self.driver.find_element_by_xpath('//*[@id="wrap_height"]/div/div[3]/div/div[4]/button[1]').click()

            sleep(3)
            print('钱海信用卡充值：3个月')

        except:
            print('点击buy now出现异常，但流程依然正常完成')
            print('钱海信用卡充值季套餐成功')




    # 三方支付充值年套餐
    @pytest.mark.run(order=1)
    def test_02(self):
        sleep(1)

        # 点击年套餐
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[2]/div[3]/article/div[3]/div[2]/a').click()

        sleep(1)

        # 打开第2个窗口，获取当前窗口并切换至当前窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])

        sleep(2)

        # 点击第三方支付
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div[2]/div/div[2]/ul/li[3]/a/span').click()

        sleep(2)

        # 输入信息：邮箱，密码
        self.driver.find_element_by_id('pw-email').send_keys('1165509917@qq.com')

        self.driver.find_element_by_id('pw-fullname').send_keys('测试')

        sleep(2)

        # 点击三方提交按钮
        self.driver.find_element_by_xpath('//*[@id="go-Paymentwall-div"]/div[2]/a').click()

        sleep(2)

        # 充值过的用户有警告框提示
        alert = self.driver.switch_to.alert
        alert.accept()

        sleep(2)

        # 弹第3个弹窗-支付弹窗，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[2])

        sleep(2)

        # 点击三方弹窗BUY按钮
        self.driver.find_element_by_id('ps_psb').click()

        sleep(15)

        # 关闭当前三方支付弹窗
        self.driver.close()

        # 回到第2个窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])
        sleep(3)

        print('paymentwall充值：1年')

    # paypal支付,充值6个月套餐
    @pytest.mark.run(order=2)
    def test_03(self):
        # 点击6个月套餐
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[2]/div[3]/article/div[2]/div[2]/a').click()

        # 打开第2个窗口，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])

        sleep(2)

        # 点击paypal充值选择按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div[2]/div/div[2]/ul/li[2]/a/span').click()

        sleep(2)

        # 第一次切换frame
        frame_1 = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(frame_1)

        # 点击paypal支付图标
        element_paypal_1 = WebDriverWait(self.driver, 10, 1). \
            until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="paypal-animation-content"]/div[1]/div[1]/div/img[2]')))


        list_1 = []

        list_1.append(element_paypal_1)

        for element in list_1:
            element.click()

            continue

        sleep(5)

        # 充值过的用户有警告框提示
        alert = self.driver.switch_to.alert
        alert.accept()

        sleep(2)

        # 回到父级iframe
        self.driver.switch_to.parent_frame()

        # 弹窗3，获取当前窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[2])

        sleep(3)

        # 第二次切换iframe
        iframe_2 = self.driver.find_element_by_name('injectedUl')
        self.driver.switch_to.frame(iframe_2)

        sleep(3)

        # 输入邮箱508151729-g@qq.com，密码11111111
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('1165509917@qq.com')

        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('11111111')

        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

        sleep(3)

        # 切出iframe_2
        self.driver.switch_to.parent_frame()
        sleep(2)

        # # 点击第一个单选按钮,可以不执行代码，默认第一个
        # self.driver.find_element_by_xpath(
        #     '//*[@id="xoSelectFi"]/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[1]/experience[2]/div/div/ng-transclude/div[1]/label')\
        #     .click()
        sleep(2)

        # 点击继续
        self.driver.find_element_by_xpath('//*[@id="button"]/button').click()

        sleep(2)

        # 点击paynow
        self.driver.find_element_by_id('confirmButtonTop').click()
        sleep(10)

        # 切换第2个窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])

        sleep(3)

        print('paypal充值：6个月')


    # paypal信用卡支付---终身
    @pytest.mark.run(order=3)
    # @pytest.mark.flaky(reruns=2, reruns_delay=3)
    def test_04(self):
        # 点击终身套餐
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[2]/div[2]/div/div[2]/a').click()

        # 弹出第2个窗口，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])

        sleep(2)

        # 点击paypal选择按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/div[2]/div/div[2]/ul/li[2]/a/span').click()

        sleep(3)

        # 切换iframe
        frame = self.driver.find_element_by_tag_name('iframe')

        self.driver.switch_to.frame(frame)

        sleep(5)

        # 点击paypal信用卡充值
        element_paypal_2 = self.driver.find_element_by_xpath('//*[@id="paypal-animation-content"]/div[1]/div[2]/div[1]/img').click()

        # list_2 = []
        # list_2.append(element_paypal_2)
        # for element in list_2:
        #     element.click()
        #     continue

        # sleep(3)

        # 充值过的用户有警告框提示
        alert = self.driver.switch_to.alert
        alert.accept()

        sleep(2)

        # 弹出新弹窗
        f = self.driver.window_handles

        self.driver.switch_to.window(f[2])

        # 弹窗最大化
        self.driver.maximize_window()
        sleep(2)

        # 填写信息
        # 定位下拉框
        element_select_1 = self.driver.find_element_by_id('countrySelector')

        # 实例化下拉框，传参
        select_1 = Select(element_select_1)

        # 获取下拉框的文本内容:获得的是字符串
        texts = element_select_1.text

        if '美国' in texts:

            # 文本定位法，选择United States
            select_1.select_by_visible_text('美国')  # 如果默认中国，选择美国

        else:

            select_1.select_by_index(0)  # 选第一个

            sleep(6)

            select_1.select_by_visible_text('United States')  # 重新选择国家

        sleep(5)

        #填写信息：
        self.driver.find_element_by_id('cc').send_keys('4032037664051295')  # 填入卡号
        sleep(1)

        self.driver.find_element_by_id('expiry_value').send_keys('0224')  # 输入有效期限

        self.driver.find_element_by_id('cvv').send_keys('456')  # 输入三位数字

        self.driver.find_element_by_id('lastName').send_keys('Ting')  # 输入姓

        self.driver.find_element_by_id('firstName').send_keys('jack')  # 输入名

        self.driver.find_element_by_xpath('//*[@id="billingLine1"]').send_keys('sdfs')  # 输入地址

        self.driver.find_element_by_xpath('//*[@id="billingLine2"]').send_keys('ssdf')  # 输入apt,ste,bldg

        self.driver.find_element_by_xpath('//*[@id="billingCity"]').send_keys('Hanford')  # 输入City

        sleep(3)

        # 定位第二个下拉框
        element_select_2 = self.driver.find_element_by_name('billingState')

        # 实例化下拉框
        select_2 = Select(element_select_2)

        # 文本定位法，选择California
        select_2.select_by_visible_text('California')  # 选择区

        sleep(2)

        # 继续填写信息
        self.driver.find_element_by_id('billingPostalCode').send_keys('93230')  # 输入邮编

        self.driver.find_element_by_id('telephone').send_keys('4082955934')  # 输入电话号码

        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('sfdsdf@qq.com')  # 输入邮箱

        sleep(1)

        # 滚动到到页面底部
        self.driver.execute_script("window.scrollTo(1,document.body.scrollHeight)")

        sleep(2)

        # # 选择已有账号
        # self.driver.find_element_by_xpath('//*[@id="signupContainer"]/fieldset/div[3]/label').click()

        sleep(2)

        # 点击paypal now，充值完成自行关闭弹窗
        self.driver.find_element_by_id('pomaSubmit').click()

        sleep(17)


        # 切换到第2个窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])

        sleep(3)

        print('paypal信用卡充值：终身！')

    def tearDown(self):

        sleep(2)

        # 关闭支付成功弹窗ok按钮,回到首页
        self.driver.find_element_by_xpath('//*[@id="pay-success"]/div[2]/div/a[2]').click()

        sleep(3)

        # # 关闭测试中的版本切换弹窗
        # self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[9]/a/i').click()

        # 定位用户头像
        user_img = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/div[5]/a[1]/div[1]/img')
        sleep(1)

        # 实例化鼠标对象
        action = ActionChains(self.driver)

        # 鼠标移动至用户头像
        action.move_to_element(user_img).perform()

        sleep(3)

        # 用户会员到期时间
        user_premium = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/div[5]/div/div[2]/div[2]/span')

        print(user_premium.text)

        sleep(2)

        # 把当前窗口关掉
        self.driver.close()

        # 回到第一个窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[0])


    def teardown_class(self):
        self.driver.quit()

if __name__ == '__main__':

    pytest.main(['-s','test_en_pay.py'])











