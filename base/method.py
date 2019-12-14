#!/usr/bin/env python
#coding:utf-8
#Author:guowanli

#以拉勾网为例,对post请求进行二次封装
import sys
sys.path.append('E:\\1test\\test1\\day13-pn1')
import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import  OperationJson

operationExcel=OperationExcel()
# print(operationExcel.get_url(3).split('/'))

def checkHeaders(row,f1=None,f2=None):
	'''检测请求头'''
	url=operationExcel.get_url(row)
	url=url.split('/')
	if url[4] == 'positionAjax.json?needAddtionalResult=false':
		return f1
	elif url[4] == 'experience':
		return f2
print(checkHeaders(3))



class Method:
	def __init__(self):
		self.json=OperationJson() #对两个类进行实例化
		self.excel=OperationExcel()

# # post请求直接读取json中data作为请求数据,使用于参数没有变化的excel用例
# 	def post(self,row):
# 		try:
# 			r=requests.post(url=self.excel.get_url(row),
# 			                data=self.json.getRequestData(row),
# 			                headers=getHeaders(),
# 			                timeout=6)
# 			return r
# 		except Exception as e:
# 			raise RuntimeError('接口请求发生未知的错误')

# post请求中用户可手动修改json中data作为请求数据
	def post(self,row,data):
		try:
			r=requests.post(url=self.excel.get_url(row),
			                data=data,
			                headers=getHeaders(),
			                timeout=6)
			return r
		except Exception as e:
			raise RuntimeError('接口请求发生未知的错误')

	# 丢弃的代码，可以用于环境版本测试（不同的环境的headers相差较大的情况下使用）
	# def post(self,row,data):
	# 	try:
	# 		r=requests.post(url=self.excel.get_url(row),
	# 		                data=data,
	# 		                headers=checkHeaders(row=row,
	# 		                                     f1=getHeaders(),
	# 		                                     f2=getHeadersInfo()),
	# 		                timeout=6)
	# 		return r
	# 	except Exception as e:
	# 		raise RuntimeError('接口请求发生未知的错误')


# 用户获取职位详情页信息，当然也可以用到其他接口中
	def get(self,url,params=None):  #有时候有的get请求有params参数，所以可以写上
		r=requests.get(url=url,
		               params=params,
		               headers=getHeaders(),
		               timeout=6)
		return r

class IsContent():
	def __init__(self):
		self.excel=OperationExcel()
	def isContent(self,row,str2):
		flag=None
		if self.excel.get_expect(row) in str2:
			flag=True
		else:
			flag=False
		return flag