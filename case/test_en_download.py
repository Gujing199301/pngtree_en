# 导包
# noinspection PyUnresolvedReferences
import time
from selenium import webdriver

from time import sleep

from selenium.webdriver import ActionChains

import unittest

import pytest

# noinspection PyUnresolvedReferences
import allure


class TestEnDownload(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()

        options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(chrome_options=options)

        # 创建浏览器对象
        # self.driver = webdriver.Chrome()

        # 英语首页
        url = "https://pngtree.com/"

        # 打开谷歌浏览器
        self.driver.get(url)

        # 设置隐式等待时间10s
        self.driver.implicitly_wait(10)

        # 浏览器窗口最大化
        self.driver.maximize_window()

        # 点击登录按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div[1]/div[2]/div[2]/a[1]').click()

        # 输入用户名，密码，点击登录
        self.driver.find_element_by_id('base-public-login-email-text').send_keys("gujingqwertyuiop@gmail.com ")

        self.driver.find_element_by_id('base-public-login-password-text').send_keys("1165509917@qq.com ")

        self.driver.find_element_by_id('base-sub-Login-Btn').click()

        sleep(3)

        # 新窗口打开测试权限
        js = 'window.open("https://pngtree.com/test?pass=zxcvb")'

        self.driver.execute_script(js)

        # 切换至新窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])

        # 点击归0当天下载数量
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[8]/td[2]/a').click()
        sleep(2)

        # 清除VIP
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a').click()
        sleep(2)

        # 刷新pv
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/a').click()
        sleep(2)

        # 关闭测试权限窗口
        self.driver.close()

        # 切换回原来窗口-首页
        self.driver.switch_to.window(f[0])
        sleep(3)

        # 防止优惠券遮罩，刷新2次页面
        self.driver.refresh()
        sleep(2)

        self.driver.refresh()
        sleep(3)

    # 普通用户使用免费机会下载收费素材-模板和字体-弹对应限制弹窗
    @pytest.mark.run(order=8)
    @allure.step(title="普通用户下载付费素材")
    def test_en_download_free_01(self):

        # 点击导航栏模板品类名，至模板分类页
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div[1]/div[1]/ul/li[3]/a').click()

        # 点击第2张模板素材
        self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[1]/div/a').click()

        # 打开第2个窗口，到达模板详情页，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])
        sleep(2)

        # 点击下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/section/div[2]/div[1]/a').click()

        sleep(3)

        # 截图，弹模板下载限制弹窗
        self.driver.get_screenshot_as_file(
            '././img/English_download_free_011.png')


        # 关闭弹窗
        self.driver.find_element_by_xpath('//*[@id="tpl-download-window-new"]/div[2]/div/a[1]/i').click()
        sleep(2)

        # 点击字体品类
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div[1]/div/div[1]/ul/li[4]/a').click()
        sleep(2)

        # 到达字体分类页，点击第2个字体素材
        self.driver.find_element_by_xpath('//*[@id="v2-content"]/div[2]/div[2]/div/ul/li[2]/div[2]/a').click()

        # 到达字体详情页，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[2])

        sleep(2)

        # 点击下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/section/div[2]/div[1]/a[1]').click()

        sleep(3)

        # 截图，弹收费素材下载限制弹窗
        self.driver.get_screenshot_as_file(
            '././img/English_download_free_012.png')

        # 关闭弹窗
        self.driver.find_element_by_xpath('//*[@id="tpl-download-window-new"]/div[2]/div/a[1]/i').click()

        sleep(2)


    # 普通用户免费下载限制/压缩包限制
    @pytest.mark.run(order=9)
    @allure.step(title="普通用户下载免费素材")
    def test_en_download_free_02(self):

        # 点击导航栏元素品类名，至元素分类页
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div[1]/div[1]/ul/li[1]/a').click()
        sleep(2)

        # 点击第2张元素素材
        self.driver.find_element_by_xpath('//*[@id="v2-content"]/div[2]/div[2]/div/ul/li[2]/div[2]/a').click()
        sleep(2)

        # 打开第2个窗口，到达元素详情页，获取并切换至详情页
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(3)

        # 先点击压缩包格式下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[1]/section/div[2]/div[1]/a[2]').click()
        sleep(3)

        # 弹压缩包限制弹窗，截图
        self.driver.get_screenshot_as_file('././img/English_free_element02.png')

        # 关闭压缩包限制弹窗
        self.driver.find_element_by_xpath('//*[@id="tpl-download-window"]/div/div/div/span/i').click()
        sleep(2)

        # 点击元素png下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[1]/section/div[2]/div[1]/a[1]').click()

        sleep(3)

        # 截图，弹免费下载限制弹窗，2次免费下载机会
        self.driver.get_screenshot_as_file('././img/English_free_element.png')

        # 点击弹窗下载按钮
        self.driver.find_element_by_xpath('//*[@id="base-download-confirm-true"]').click()
        sleep(2)

        # 打开第3个窗口，到达下载页，获取句柄并切换至下载页
        f = self.driver.window_handles

        self.driver.switch_to.window(f[2])
        sleep(2)

        # 在下载页点击背景分类名
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/ul/li[2]/a').click()
        sleep(1)

        # 在背景分类页点击第2个背景素材
        self.driver.find_element_by_xpath('//*[@id="v2-content"]/div[2]/div[2]/div[2]/div[1]/a/img').click()
        sleep(1)

        # 打开第四个窗口，至背景详情页，获取并切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[3])

        sleep(2)

        # 点击背景压缩包格式下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/section/div[2]/div[1]/a[2]').click()
        sleep(3)

        # 弹窗压缩包下载限制弹窗，截图
        self.driver.get_screenshot_as_file('././img/English_free_background02.png')

        # 关闭压缩包下载限制弹窗
        self.driver.find_element_by_xpath('//*[@id="tpl-download-window"]/div/div/div/span/i').click()
        sleep(2)

        # 点击背景png/jpg等格式下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/section/div[2]/div[1]/a[1]').click()

        sleep(3)

        # 截图，弹免费下载限制弹窗，1次免费下载机会
        self.driver.get_screenshot_as_file('././img/English_free_background.png')

        # 点击弹窗下载按钮
        self.driver.find_element_by_xpath('//*[@id="base-download-confirm-true"]').click()

        sleep(2)

        # 打开第5个窗口，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[4])

        sleep(2)

        # 在第5个窗口点击导航插画品类
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/ul/li[5]/a').click()
        sleep(1)

        # 到达插画分类页，点emotional分类词
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div[2]/div/div[1]/ul/li[1]/a').click()
        sleep(2)

        # 点击第2个插画素材
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div[2]/div/div[2]/div[2]/div[1]/a/img').click()
        sleep(1)

        # 打开第6个窗口，切换窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[5])

        sleep(2)

        # 点击下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/section/div[2]/div[1]/a[1]').click()

        sleep(3)

        # 截图---2次免费下载用完，基数uid弹老版限制弹窗
        self.driver.get_screenshot_as_file('././img/English_download_limit.png')

        # 关闭弹窗
        self.driver.find_element_by_xpath('//*[@id="downastrict-2"]/div[2]/div/a[1]/i').click()
        sleep(2)


    # 会员下载付费素材
    @pytest.mark.run(order=10)
    @allure.step(title="会员下载付费素材")
    def test_en_download_premium(self):

        # 点击导航栏充值入口
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div[1]/div[1]/ul/li[8]/a/span').click()

        sleep(3)

        # 点击季套餐
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[2]/div[3]/article/div[1]/div[2]/a').click()

        # 打开第2个窗口，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])
        sleep(2)

        # 获取页面订单价格
        price = self.driver.find_element_by_xpath(
            '//*[@id="wrapper"]/div[3]/div/div[2]/div/div[1]/div/div[3]/span[2]/span[2]')
        print(price.text)

        sleep(1)

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

        # 充值成功有提示文案
        payment_success = self.driver.find_element_by_xpath('//*[@id="ps_content"]/h3')

        # 打印文案
        print(payment_success.text)

        sleep(2)

        # 关闭当前三方支付弹窗
        self.driver.close()

        # 回到第2个窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[1])
        sleep(3)

        # 关闭支付成功弹窗ok按钮,回到首页
        self.driver.find_element_by_xpath('//*[@id="pay-success"]/div[2]/div/a[2]').click()

        sleep(3)

        # 点击导航栏模板品类名，至模板分类页
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[1]/div[1]/ul/li[3]/a').click()

        # 点击第2张模板素材
        self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[1]/div/a').click()

        # 打开第2个窗口，到达模板详情页，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[2])
        sleep(2)

        # 点击下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/section/div[2]/div[1]/a').click()

        sleep(3)

        # 直接下载，到达下载页
        f = self.driver.window_handles
        self.driver.switch_to.window(f[3])
        sleep(1)

        # 截图--底部1张下载
        self.driver.get_screenshot_as_file(
            '././img/English_download_premium_01.png')

        sleep(3)

        # 点击字体品类
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/ul/li[4]/a').click()
        sleep(2)

        # 到达字体分类页，点击第2个字体素材
        self.driver.find_element_by_xpath('//*[@id="v2-content"]/div[2]/div[2]/div/ul/li[2]/div[2]/a').click()

        # 到达字体详情页，切换窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[4])

        sleep(2)

        # 点击下载按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div/section/div[2]/div[1]/a[1]').click()

        sleep(3)

        # 直接下载，到达下载页
        f = self.driver.window_handles
        self.driver.switch_to.window(f[5])
        sleep(1)

        # 截图，弹收费素材下载限制弹窗
        self.driver.get_screenshot_as_file(
            '././img/English_download_premium_02.png')
        sleep(2)

        # 页面下拉
        js = 'window.scrollTo(0,300)'
        self.driver.execute_script(js)
        sleep(2)

        # 点击1张推荐图,到详情页（也可能是下架页）
        self.driver.find_element_by_xpath('//*[@id="recommend-id-down"]/div/div/div/ul/li[1]/div[1]/a').click()
        sleep(1)

        # 打开了一个新窗口，切换窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[6])

        sleep(2)

        # 新窗口打开测试权限
        js = 'window.open("https://pngtree.com/test?pass=zxcvb")'

        self.driver.execute_script(js)

        sleep(1)

        # 切换至新窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[7])

        # 操作2-点击清除vip
        self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a').click()
        sleep(2)

        # 关闭当前窗口
        self.driver.close()

        # 切换回原窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[6])
        sleep(1)

    def tearDown(self):

        # 点击元素品类名到元素分类页，均为旧导航
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/section/div[1]/div/div[1]/ul/li[1]/a').click()
        sleep(2)

        # 点击logal回到首页
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/a').click()

        sleep(2)

        # 定位用户头像
        user_img = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div[1]/div[2]/div[5]/a[1]/div/img')


        # 实例化鼠标对象
        action = ActionChains(self.driver)

        # 鼠标移动至用户头像
        action.move_to_element(user_img).perform()

        sleep(3)

        # 截图
        self.driver.get_screenshot_as_file(
            '././img/English_download_left.png')

        # 关闭浏览器
        sleep(2)

        self.driver.quit()









