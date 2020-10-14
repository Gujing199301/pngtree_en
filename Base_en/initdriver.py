from selenium import webdriver


def get_driver():

    chromeOptions = webdriver.ChromeOptions()

    # 设置代理
    chromeOptions.add_argument("--proxy-server=http://127.0.0.1:1080")
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    # 返回浏览器驱动对象
    return driver
