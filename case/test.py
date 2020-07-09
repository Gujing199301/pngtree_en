import pytest

import allure

import unittest


class TestAdd(unittest.TestCase):

    @allure.step(title='登录功能')
    def test_01(self):
        print('第一条测试用例')

    @allure.step(title='下载功能')
    def test_02(self):
        print('第二条测试用例')

if __name__ == '__main__':
    pytest.main(['-s','test.py'])
