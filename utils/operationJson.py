#!/usr/bin/env python
#coding:utf-8
#Author:guowanli


#对json文件的操作,读取到文件内容
import sys
sys.path.append('E:\\1test\\test1\\day13-pn1')
import json
from  utils.public import *
from utils.operationExcel import OperationExcel

class OperationJson:
	def __init__(self):
		self.excel=OperationExcel()    #继承OperationExcel类的方法，这里是是对类的实例化处理

	def getReadJson(self):
		# 读取json文件
		# 读取过程中遇到json.decoder.JSONDecodeError，需要将json文件中的False改为"false"
		with open(data_dir('data','requestData.json'),'r',encoding='utf-8') as f:
			# print(type(json.load(f)))  #多了这行代码会出错，数据类型为字典
			return json.load(f)

	def getRequestData(self,row):
		'''
		取请求参数
		json.dumps()将字典处理为json
		'''
		return json.dumps(self.getReadJson()[self.excel.get_request_data(row)])

# opera=OperationJson()
# print(opera.getRequestData(1))

# a='\u81ea\u52a8\u5316\u6d4b\u8bd5'
# print(type(a))
# print(str(a))
# print(type(a))
# print(bytes(a,encoding='gb2312'))
# print(type(a))