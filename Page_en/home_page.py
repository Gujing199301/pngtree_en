from time import sleep
from Base_en.base import Base
import Page_en
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_login(self):

        # 点击首页登录按钮
        self.click_element(Page_en.home_login_xpath)

    def click_logout(self):

        # 创建鼠标操作对象
        action = ActionChains(self.driver)
        # 定位普通用户头像
        element_free_user_img = self.search_element(Page_en.home_free_user_img_xpath)
        # 鼠标悬停至普通用户头像
        action.move_to_element(element_free_user_img).perform()
        sleep(3)
        # 点击退出登录
        self.click_element(Page_en.home_logout_xpath)

    def screen_user_vip(self):
        # 创建鼠标操作对象
        action = ActionChains(self.driver)
        # 定位VIP用户头像
        element_vip_user_img = self.search_element(Page_en.home_vip_user_img_xpath)
        # 鼠标悬停至用户头像
        action.move_to_element(element_vip_user_img).perform()
        sleep(5)
        # 截图
        self.screen_shot('VIP-')
        sleep(1)








