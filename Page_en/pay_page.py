import Page_en
from Base_en.base import Base
from time import sleep
from  selenium.webdriver.support.select import Select


class PayPage(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def card_pay(self):

        # 切换到支付页
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        # 打开支付页默认钱海信用卡渠道
        # self.click_element(Page_en.pay_card_xpath)
        self.send_element(Page_en.card_first_name_id,'姓氏')
        self.send_element(Page_en.card_last_name_id,'名字')
        self.send_element(Page_en.card_phone_number_id,'123456')
        self.send_element(Page_en.card_city_id,'上海')
        self.send_element(Page_en.card_email_id,'1165509917@qq.com')
        self.send_element(Page_en.card_postal_code_id,'310000')
        self.send_element(Page_en.card_billing_address_id,'浦东')
        sleep(5)
        # 提交订单
        self.click_element(Page_en.card_confirm_subscription_button_id)
        sleep(3)

        # 24小时之内充值过的用户有警告框提示
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            sleep(1)

        except AssertionError:
            print('无需操作')

        finally:
            # 切换frame
            frame_1 = self.driver.find_element_by_id('ifrm_creditcard_checkout')
            self.driver.switch_to.frame(frame_1)
            sleep(3)
            # 输入卡号等信息
            self.send_element(Page_en.card_card_number_id,'4111119987834534')
            sleep(1)
            self.send_element(Page_en.card_expiration_date_id,'02/24')
            sleep(1)
            self.send_element(Page_en.card_secure_code_id,'789')
            sleep(2)
            # 点击pay now按钮
            self.click_element(Page_en.card_pay_now_xpath)
            sleep(10)

    def paypal_pay(self):

        # 切换到支付页
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(2)
        # 刷新页面
        self.driver.refresh()
        sleep(3)
        # 选择paypal支付方式
        self.click_element(Page_en.pay_paypal_xpath)
        sleep(4)
        # 第一次切换frame
        frame_1 = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(frame_1)
        sleep(1)
        # 点击paypal支付图标
        self.click_element(Page_en.paypal_icon_xpath)
        sleep(3)
        # 充值过的用户有警告框提示
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(6)
        # 弹窗3，获取当前窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[2])
        sleep(3)
        try:
            # 第二次切换iframe
            iframe_2 = self.driver.find_element_by_name('injectedUl')
            self.driver.switch_to.frame(iframe_2)
            sleep(2)
            # 输入邮箱1165509917@qq.com，密码11111111
            self.send_element(Page_en.paypal_email_id, '1165509917@qq.com')
            self.send_element(Page_en.paypal_password_id, '11111111')
            sleep(1)
        except:
            # 如果出现让登陆paypal账号,点击登录
            self.click_element(Page_en.paypal_go_login_xpath)
            sleep(1)
            # 输入账号
            self.send_element(Page_en.paypal_email_id, '1165509917@qq.com')
            sleep(2)
            # 输入下一步
            self.click_element(Page_en.paypal_next_xpath)
            sleep(2)
            # 输入密码
            self.send_element(Page_en.paypal_password_id, '11111111')
            sleep(1)
        finally:

            # 点击登录
            self.click_element(Page_en.paypal_login_xpath)
            sleep(3)
            # 切出iframe
            self.driver.switch_to.default_content()
            sleep(2)
            # 点击继续
            self.click_element(Page_en.paypal_continue_xpath)
            sleep(2)
            # 点击paynow
            self.click_element(Page_en.paypal_buy_now_id)
            sleep(10)
            # 切换第2个窗口
            f = self.driver.window_handles
            self.driver.switch_to.window(f[1])
            sleep(3)

    def pw_pay(self):

        # 切换到支付页
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(2)
        # 选择本地支付方式
        self.click_element(Page_en.pay_paymentwall_xpath)
        sleep(10)
        # 输入信息并添加订单
        self.send_element(Page_en.pw_input_email_id, '1165509917@qq.com')
        sleep(1)
        self.send_element(Page_en.pw_input_password_id, '123456')
        sleep(1)
        self.click_element(Page_en.pw_confirm_subscription_xpath)
        sleep(5)
        # 24小时之内充值过有提示框
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(3)
        # 弹窗3，获取当前窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[2])
        sleep(3)
        # 点击窗口3中的buy now按钮
        self.click_element(Page_en.pw_buy_now_button_id)
        sleep(15)
        # 支付成功后弹窗3中有提示文案
        pw_pay_success = self.search_element(Page_en.pw_pay_success_xpath)
        print(pw_pay_success.text)
        sleep(2)
        # 关闭当前窗口3
        self.driver.close()

    def paypal_card_pay(self):

        # 切换到支付页
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(2)
        # 刷新页面
        self.driver.refresh()
        sleep(3)
        # 选择paypal支付方式
        self.click_element(Page_en.pay_paypal_xpath)
        sleep(4)
        # 第一次切换frame
        frame_1 = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to.frame(frame_1)
        sleep(1)
        # 点击paypal信用卡支付图标
        self.click_element(Page_en.paypal_card_icon_xpath)
        sleep(1)
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
        # 定位下拉框1选择国家
        element_select_1 = self.search_element(Page_en.paypal_card_country_select_id)
        # 实例化下拉框，传参
        select_1 = Select(element_select_1)
        # 获取下拉框的文本内容:获得的是字符串
        texts = element_select_1.text
        sleep(2)
        if '美国' in texts:
            # 文本定位法，选择United States
            select_1.select_by_visible_text('美国')  # 选择国家
        else:
            select_1.select_by_visible_text('United States')  # 选择国家
        sleep(5)
        # 输入信息
        self.send_element(Page_en.paypal_card_card_number_id, '4032037664051295')  # 填入卡号
        self.send_element(Page_en.paypal_card_expory_id, '0224')  # 输入有效期限
        self.send_element(Page_en.paypal_card_cvv_id, '666')  # 输入三位有效数字
        self.send_element(Page_en.paypal_card_first_name_id, 'Ting')  # 输入姓
        self.send_element(Page_en.paypal_card_last_name_id, 'jack')  # 输入名
        sleep(1)
        self.send_element(Page_en.paypal_card_address1__id, 'address1')  # 输入地址1
        self.send_element(Page_en.paypal_card_address2__id, 'address2')  # 输入地址2
        self.send_element(Page_en.paypal_card_city_id, 'Handford')  # 输入城市
        sleep(3)

        # 定位第二个下拉框2选择洲
        element_select_2 = self.driver.find_element_by_name('billingState')
        # 实例化下拉框
        select_2 = Select(element_select_2)
        # 文本定位法，选择California
        select_2.select_by_visible_text('California')  # 选择区

        # 继续填写信息
        self.send_element(Page_en.paypal_card_poster_code__id, '93230')  # 输入邮编
        self.driver.find_element_by_id('telephone').send_keys('4082955934')  # 输入电话号码
        self.send_element(Page_en.paypal_card_email_xpath, '1165509917@qq.com')  # 输入邮箱
        sleep(1)
        # 滚动到到页面底部
        self.driver.execute_script("window.scrollTo(1,document.body.scrollHeight)")
        sleep(2)
        # 点击paypal now，充值完成自行关闭弹窗
        self.click_element(Page_en.paypal_card_buy_now_id)
        sleep(20)















