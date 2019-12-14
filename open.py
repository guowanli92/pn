#!/usr/bin/env python
#coding:utf-8
#Author:guowanli

'''实现对请求参数按key=value的格式按ASCII字典排序，在这个基础上尾部拼接密钥，然后进行md5加密'''
'''md5很难破解，加上我们不知道密钥是怎么写的'''
from urllib import parse
import hashlib

# 1、动态参数 2、ASCII排序
def dataSign(secure="ruolin",*args,**kwargs):
	dict1=dict(sorted(kwargs.items(),key=lambda item:item[0]))    #拿key来进行ASCII排序，0代表字典中key,如果要取value,就要用1
# 3、字典拼接 4、添加密钥
	str1=parse.urlencode(dict1)+secure
	# print(str1)  #结果为a=a&age=18&b=b&c=c&name=ruolinruolin
# 5、md5加密
	m2=hashlib.md5()   #实例化md5
	m2.update(str1.encode('utf-8'))
	return m2.hexdigest()

dict2={"a":"a","c":"c","b":"b","name":"ruolin","age":18}
print(dataSign(**dict2)) #调用字典，**必须要有   #结果为3e9667b25dd914cf1452306deafc0cee

