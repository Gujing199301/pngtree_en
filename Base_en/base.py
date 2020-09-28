import allure,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver

    def search_element(self,loc,timeout=15,poll_frequency=1.0):
        """
        定位单个元素
        :param loc:定位类型 (By.ID,id属性值) (By.CLASS_NAME,class属性) (By.XPATH,xpath属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隙
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))

    def search_elements(self,loc,timeout=15,poll_frequency=1.0): # {"ty":xx,"value":xxx} (ty,value)
        """
        定位一组元素
        :param loc:定位类型 (By.ID,id属性值) (By.CLASS_NAME,class属性) (By.XPATH,xpath属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隙
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))

    def click_element(self,loc,timeout=15,poll_frequency=1.0):
        """
        点击元素
        :param loc:定位类型 (By.ID,id属性值) (By.CLASS_NAME,class属性) (By.XPATH,xpath属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隙
        :return:
        """
        self.search_element(loc,timeout,poll_frequency).click()

    def send_element(self,loc,text,timeout=15,poll_frequency=1.0):
        """
        输入内容
        :param loc:定位类型 (By.ID,id属性值) (By.CLASS_NAME,class属性) (By.XPATH,xpath属性值)
        :param text:输入文本内容
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隙
        :return:
        """

        # 定位元素
        input_text = self.search_element(loc,timeout,poll_frequency)
        # 清空元素
        input_text.clear()
        # 输入内容
        input_text.send_keys(text)

    def screen_shot(self,name):
        """
        截图
        :param name: 展示截图名字
        :return:
        """
        # 定义图片名字
        png_name = "././screen/"+name+"{}.png".format(int(time.time()))
        # 截取图片
        self.driver.get_screenshot_as_file(png_name)

        # # 图片添加至报告
        # with open(png_name,"rb") as f:
        #     allure.attach(name,f.read(),allure.attach_type.PNG)






















