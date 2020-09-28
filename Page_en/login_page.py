from Base_en.base import Base
import Page_en
from time import sleep


class LoginPage(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def email_login(self,username,password):

        # 输入邮箱
        self.send_element(Page_en.login_email_username_id,username)
        sleep(1)
        # 输入密码
        self.send_element(Page_en.login_email_password_id,password)
        sleep(1)
        # 点击登录
        self.click_element(Page_en.login_email_button_id)
        sleep(3)

    def fb_login(self,username,password):

        # 点击fb登录入口
        self.click_element(Page_en.login_fb_icon_xpath)
        sleep(3)

        # 切换fb登录窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(3)

        # 输入用户名
        self.send_element(Page_en.login_fb_username_xpath, username)
        sleep(1)
        # 输入密码
        self.send_element(Page_en.login_fb_password_xpath, password)
        sleep(1)
        # 点击登录
        self.click_element(Page_en.login_fb_button_xpath)
        sleep(5)
        # 登录完成后窗口自动关闭，切换回原来窗口
        self.driver.switch_to.window(f[0])
        sleep(3)

    def twitter_login(self,username,password):

        # 点击twitter登录入口
        self.click_element(Page_en.login_twitter_icon_xpath)
        sleep(3)

        # 切换twitter登录窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(3)
        # 输入用户名
        self.send_element(Page_en.login_twitter_username_id,username)
        sleep(1)
        # 输入密码
        self.send_element(Page_en.login_twitter_password_id,password)
        sleep(1)
        # 点击登录按钮
        self.click_element(Page_en.login_twitter_button_id)
        sleep(3)

        # 登录完成窗口自行关闭，切换回原来窗口
        self.driver.switch_to.window(f[0])
        sleep(3)









