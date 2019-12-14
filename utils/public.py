#!/usr/bin/env python
#coding:utf-8
#Author:guowanli

#读取文件
import os

def data_dir(dirName,fileName):
	# 上一级目录+目录名+文件名
	'''查找文件的路径'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),dirName,fileName)

# print(data_dir('config','config.ini'))