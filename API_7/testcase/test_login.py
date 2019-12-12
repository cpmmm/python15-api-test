# -*- coding: utf-8 -*-
'''
@time: 2019/11/29 0029 16:26
@author: chen
@contact: 1171954100@qq.com
@file: test_login.py
@desc:
        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +

'''
import unittest
from API_7.common.http_request2 import HTTPRequest2
from API_7.common import do_excel
from API_7.common import contants
from ddt import ddt,data             #没导入ddt会执行一条结果，然而写了6条

@ddt
class TestLogin(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'TestLogin')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()

    @data(*cases)                    #data可以接收可迭代数据类型，列表，元组，字典
    def test_login(self,case):
        print(case.title)
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,"pass")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "fail")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()