#!/usr/bin/env python
#coding:utf-8
#Author:guowanli

#对excel文件的操作，读取到excel中文件的内容，中间考虑到：
#1、读取文件的公共代码的分离
#2、excel用例中易变、不易变的数据的分离

import sys
sys.path.append('E:\\1test\\test1\\day13-pn1')
import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_data import *

class OperationExcel:   #没什么可继承的，就不用加()
	'''获取文件和sheet'''
	def getExcel(self):
		db=xlrd.open_workbook(data_dir('data','data.xls'),'r')
		sheet=db.sheet_by_index(0)
		return sheet

	def get_rows(self):
		'''获取sheet的行数'''
		return self.getExcel().nrows    # nrows表示number of rows,sheet的总行数

	def get_row_cel(self,row,col):
		'''获取单元格的内容'''
		return self.getExcel().cell_value(row,col)    #row：行，col:列,都是从0开始的索引

	def getCaseID(self,row):
		'''获取测试ID'''
		return self.get_row_cel(row,getCaseID)

	def get_url(self,row):
		'''获取请求地址'''
		return self.get_row_cel(row,getUrl())

	def get_request_data(self,row):
		'''获取请求参数'''
		return self.get_row_cel(row,get_request_data())

	def get_expect(self,row):
		'''获取期望结果'''
		return self.get_row_cel(row,getExpect())

	def get_result(self,row):
		'''获取实际结果'''
		return self.get_row_cel(row,getResult())

# opera=OperationExcel()
# print(opera.get_expect(1))


	def writeResult(self,row,content):
		'''在Excel中写入测试结果'''
		col=getResult() #获取实际结果所在的列
		'''excel文件内容的修改--xlutils'''
		work = xlrd.open_workbook(data_dir('data','data.xls'),'r')  # 1、找到要修改的对象
		old_content = copy(work)  # 2、复制文件的内容
		ws = old_content.get_sheet(0)  # 3、找到要修改的sheet
		ws.write(row,col,content)  # 4、修改具体的值
		old_content.save(base_dir('data','data.xls'))  # 5、保存内容到指定的文件中，文件名可以自定义


	def run_success_result(self):
		'''获取成功的测试用例数'''
		pass_count=[]
		fail_count=None
		for i in range(1,self.get_rows()):   #self.get_rows()应该改为self.get_rows()+1？不应该加1，因为get_rows()统计的是真实的行数
			if self.get_result(i)=='pass':   #而get_result()中的i是传入的索引，所以无需加1
				pass_count.append(i)
		return int(len(pass_count))

	def run_fail_result(self):
		'''获取执行失败的测试用例数'''
		return int((self.get_rows()-1)-self.run_success_result())

	def run_pass_rate(self):
		'''测试结果通过率'''
		rate=''
		if self.run_fail_result()==0:
			rate='100%'
		elif self.run_fail_result()!=0:
			rate=str(int(self.run_success_result()/(self.get_rows()-1)*100))+'%'
		return rate

opera=OperationExcel()
print(opera.run_success_result())
print(opera.run_fail_result())
print(opera.run_pass_rate())


