import pytest
import unittest
import allure


class TestAdd:
    @allure.step(title = '登录功能')
    def test_01(self):
        print('登录成功')
        assert True

    @allure.step(title = '充值功能')
    def test_02(self):
        print('充值成功')
        assert False








