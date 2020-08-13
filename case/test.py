# 导包
import time
from time import sleep
from selenium import webdriver
import pytest
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class TestEnLogin(unittest.TestCase):

    # 初始化操作
    def setup_class(self):

        # 创建浏览器对象
        self.driver = webdriver.Chrome()

        url = "https://www.baidu.com/"

        # 谷歌浏览器打开测试权限
        self.driver.get(url)

        # 浏览器窗口最大化
        self.driver.maximize_window()


    def setUp(self):

        sleep(2)
        print('开始')

    # email登录
    def test_baidu(self):
        # 输入搜素词
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("java")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="su"]').click()

        sleep(1)

    def tearDown(self):

        print('结束')

    def teardown_class(self):
        sleep(2)
        self.driver.quit()




