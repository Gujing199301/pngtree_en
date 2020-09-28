import Page_en
from Base_en.base import Base
from time import sleep

class Testpage(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)


    def flush_pv(self):
        # 刷新pv
        self.click_element(Page_en.test_flush_pv_xpath)
        sleep(2)

    def clear_vip(self):
        # 清除vip
        self.click_element(Page_en.test_clear_vip_xpath)
        sleep(2)

    def flush_score(self):
        # 变成第一天登录
        self.click_element(Page_en.test_flush_score_xpath)
        sleep(2)

    def change_c_time(self):
        # 修复注册时间为今天
        self.click_element(Page_en.test_change_c_time_xpath)
        sleep(1)
