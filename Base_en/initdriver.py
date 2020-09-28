from selenium import webdriver


def get_driver():

    # 创建浏览器对象
    driver = webdriver.Chrome()

    # 返回浏览器驱动对象
    return driver
