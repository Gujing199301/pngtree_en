# noinspection PyUnresolvedReferences
import pytest

import unittest

# noinspection PyUnresolvedReferences
import allure


class TestAdd(unittest.TestCase):

    @allure.step(title='测试登录')
    def test_01(self):

        allure.attach('点击登录，输入用户名密码，登录')
        print('登录')

    @allure.step(title='测试充值')
    def test_02(self):

        allure.attach('使用钱海充值')
        print('充值')
