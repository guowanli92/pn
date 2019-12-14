#!/usr/bin/env python
#coding:utf-8
#Author:guowanli

#excel中列中的东西可以定义为一个变量，在主代码中针对列已有相应的处理，在传递参数的时候只需要传具体是哪一行就行了
#存的纯粹是函数,因此无需在本文件中找到具体xls文件

class ExcelVariable:
	'''将EXCEL中的列转化为变量'''
	caseID=0    #索引
	url=2
	request_data=3
	expect=4
	result=5

def getCaseID():
	return ExcelVariable.caseID #类属性

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def getExpect():
	return ExcelVariable.expect

def getResult():
	return ExcelVariable.result

def getHeaders():
	'''获取请求头'''
	headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	           'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
	           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
	           'Cookie': 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1575691444,1575768475; _ga=GA1.2.34149370.1575691445; user_trace_token=20191207120404-9b95e78e-18a6-11ea-a695-5254005c3644; LGUID=20191207120404-9b95ef07-18a6-11ea-a695-5254005c3644; _gid=GA1.2.1356957470.1575691445; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=e637b55ab497438db0934dc0276a72d7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ede88101c6c7-0a0372c86149178-14636e4a-2073600-16ede88101d44b%22%2C%22%24device_id%22%3A%2216ede88101c6c7-0a0372c86149178-14636e4a-2073600-16ede88101d44b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; JSESSIONID=ABAAABAAAGGABCB9D454FDC7F5D6979F1365A651CDF1587; X_HTTP_TOKEN=8244e42e9085fc292848675751aa760bc24cacb4c0; WEBTJ-ID=20191208092753-16ee31ebf2119-0e4d98cb230187-14636e4a-2073600-16ee31ebf2317b; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1575768475; _gat=1; LGSID=20191208092754-f5360c01-1959-11ea-abb6-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGRID=20191208092754-f5360d72-1959-11ea-abb6-525400f775ce; X_MIDDLE_TOKEN=d8dd9efbb36a5cfceba753f64de44b04'}
	return headers


# 放弃的代码
# def getHeadersInfo(positionID=None):
# 	'''点击进入某职位的请求头'''
# 	headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# 	           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
# 	           'Cookie': 'SEARCH_ID=75f874c9c04b40009bf2a32eabdaa010; JSESSIONID=ABAAABAAAFCAAEG915136547C7689A7091203B4D50524A2; WEBTJ-ID=20191208091236-16ee310c13bcf-0d4e48beb984d1-71415a3b-2073600-16ee310c13e5d; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1575683073,1575683082,1575688243,1575767557; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20191207094432-1d8af12e-1893-11ea-a695-5254005c3644; PRE_SITE=; LGSID=20191208150032-6d4701c4-1988-11ea-abc1-525400f775ce; user_trace_token=20191207094430-f3051a7d-4a25-438f-ada3-93db84feea5f; _gat=1; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ede089b86d4-0ad3c7218d1e96-71415a3b-2073600-16ede089b8710%22%2C%22%24device_id%22%3A%2216ede089b86d4-0ad3c7218d1e96-71415a3b-2073600-16ede089b8710%22%7D; _gid=GA1.2.1598569676.1575683083; _ga=GA1.2.1664592437.1575683073; PRE_HOST=; PRE_UTM=; X_HTTP_TOKEN=05a1eee1b8f0d6a434688757511df1ae62cf5369c1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1575788636; LGRID=20191208150356-e671082e-1988-11ea-abc1-525400f775ce',
# 	           'Referer':'https://www.lagou.com/jobs/5966626.html?show=1dcbec0cfa264c4899fb5a3d84ce4745'}
# 	return headers

