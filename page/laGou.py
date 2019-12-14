#!/usr/bin/env python
#coding:utf-8
#Author:guowanli

#对象层代码
import sys
sys.path.append('E:\\1test\\test1\\day13-pn1')
from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel
import json
from  utils.public import *

operationJson=OperationJson()
operationExcel=OperationExcel()

#获取到json数据，对kd(搜索关键字)进行赋值
def setSo(kd=None):   #函数的参数有默认值，此处给None,表示不确定，也可以给一个默认值
	'''对搜索的数据重新赋值'''
	dici1=json.loads(operationJson.getRequestData(1))
	# print(dici1,type(dici1))  #{"first": "true", "kd": "\u81ea\u52a8\u5316\u6d4b\u8bd5", "pn": 1} <class 'str'>
	dici1['kd']=kd  #对json文件中的数据进行重新赋值
	return dici1
# print(setSo('性能测试工程师'))

def writePositionId(content):
	'''把职位的ID写到文件中'''
	with open(data_dir(dirName='data',fileName='positionId'),'w') as f:
		f.write(content)

def getPositionId():
	'''读取文件职位招聘的信息（通过职位ID）'''
	with open(data_dir(dirName='data',fileName='positionid'),'r') as f:
		return json.loads(f.read())
		# f.read()   #f.read()获取的数据为字符串


def setpositionInfo(row):
	dict1=json.loads(operationJson.getRequestData(row))
	dict1['positionId']=getPositionId()[0]
	return dict1

def getUrl(positionId):
	urlInfo=operationExcel.get_url(4)
	userInfo='https://www.lagou.com/jobs/{0}.html?show=1dcbec0cfa264c4899fb5a3d84ce4745'.format(positionId)
	return userInfo
# print(getUrl(getPositionId()))

