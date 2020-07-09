# 导包
from selenium import webdriver

import unittest

from time import sleep

import time

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys



class Test_English_search(unittest.TestCase):

    def setUp(self):

        # 创建浏览器对象
        self.driver = webdriver.Chrome()

        # 打开谷歌浏览器
        self.driver.get("https://pngtree.com/")

        # 浏览器窗口最大化
        self.driver.maximize_window()

        # 设置隐式等待时间10s
        self.driver.implicitly_wait(10)

        sleep(2)

    def test_E_search(self):

        # 点击导航栏元素品类
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/ul/li[2]/a').click()
        sleep(2)

        # 到元素分类页，点击animals
        self.driver.find_element_by_xpath('//*[@id="v2-content"]/div[2]/div[1]/div[4]/div/div[2]/a').click()
        sleep(2)

        # 点击elephant
        self.driver.find_element_by_xpath('//*[@id="v2-content"]/div[2]/div[1]/div[5]/div/div[14]/a').click()

        sleep(2)

        js = 'window.scrollTo(10000,0)'
        js = 'window.scrollTo(10000,4300)'

        self.driver.execute_script(js)

        sleep(2)

        # 点击下一页
        self.driver.find_element_by_xpath('//*[@id="v2-content"]/div[2]/div[3]/div/a[11]').click()

        # 输入搜素词free,点击搜索按钮
        self.driver.find_element_by_xpath('//*[@id="v2-subpageBan"]/div/div/form/input').send_keys('free')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="v2-subpageBan"]/div/div/form/a/i').click()

        # 到达元素搜索页

        # 给一些搜素热词
        list_search = ['flower','tree','coffee','card','music']

        for search in list_search:

            # 定位搜索框，清空，输入搜索词
            search_input = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div[2]/input')

            # 清空搜索框
            search_input.clear()
            sleep(2)

            # 输入搜索词tree
            search_input.send_keys(search)
            sleep(1)
            # 模拟键盘按回车ENTER
            search_input.send_keys(Keys.ENTER)
            sleep(2)



if __name__ == '__main__':
    unittest.main()
