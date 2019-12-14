#!/usr/bin/env python
#coding:utf-8
#Author:guowanli

import sys
sys.path.append('E:\\1test\\test1\\day13-pn1')
import unittest
import json
from base.method import Method,IsContent
from page.laGou import *
import utils.public
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class LaGou(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.p=IsContent()
		self.excel=OperationExcel()
		self.json=OperationJson()

	def statusCode(self,r):
		self.assertEqual(r.status_code,200)
		self.assertEqual(r.json()['code'],0)

	def isContent(self,r,row):
		self.statusCode(r)  # 注意要给statusCode传数据
		self.assertTrue(self.p.isContent(row=row,str2=r.text))

	def test_laGou_001(self):
		'''拉勾：测试翻页,第一页'''
		r=self.obj.post(row=1,data=self.json.getRequestData(row=1))   #obj这种写法的原理是什么,见setup方法
		print(r.text)
		self.isContent(r=r,row=1)  #为什么不是写成self.p.isContent(r=r,row=1)???
		self.excel.writeResult(1,'pass')



	def test_laGou_002(self,row=2):
		'''拉勾：测试翻页，第二页'''
		r=self.obj.post(2)   #obj这种写法的原理是什么,见setup方法
		self.isContent(r=r,row=row)
		self.excel.writeResult(2,'pass') #如果上面的断言失败了，pass就不会被写进文件中了


	def test_laGou_003(self, row=3):
		'''拉勾：测试翻页，传入不同类型的搜索关键字，替换json中的数据进行测试'''
		r = self.obj.post(row=3,data=setSo('性能测试工程师'))
		print(r.text)
		list1=[]
		for i in range(0,15):  # 0< <16
			positionId=r.json()['content']['positionResult']['result'][i]['positionId']
			list1.append(positionId)
		writePositionId(json.dumps(list1))
		print(list1)
		# self.isContent(r=r, row=row)


	def test_laGou_004(self, row=4):
		'''拉勾：访问搜索‘性能测试工程师’查看每个职位的详情信息'''
		for item in getPositionId():
			r=self.obj.get(url=getUrl(positionId=item))
			# print(r.url)
			print(r.text)  #因为返回的详情页面是html的，所以没有响应状态码，只需要断言数据就行
			self.assertTrue(self.p.isContent(row=4,str2=r.text))  #要么写成(row=4,str2=r.text)，要么写成(4,r.text),否则报错




if __name__ == '__main__':
	unittest.main(verbosity=2)