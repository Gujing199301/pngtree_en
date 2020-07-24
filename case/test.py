# noinspection PyUnresolvedReferences
import pytest

import unittest

# noinspection PyUnresolvedReferences
import allure


class TestAdd(unittest.TestCase):

    @allure.step(title='测试登录')
    def test_01(self):
        
        print('登录')

    @allure.step(title='测试充值')
    def test_02(self):

        print('充值')
