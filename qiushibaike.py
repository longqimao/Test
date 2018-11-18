#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 19:58

import requests
from lxml import etree
page=1
while True:
	url = 'https://www.qiushibaike.com/8hr/page/'+str(page)
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
					 '(KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
	}
	res = requests.get(url,headers=headers)
	res = res.text
	html = etree.HTML(res)
	result =html.xpath ('//a/div[@class="content"]/span/text()')
	print(result)
	length = len(result)

	page += 1
	if page==13:
		break
	else:
		continue
print(length)
for j in range(0,length):
	fileHandle = open("relust1.txt",'a',encoding='utf-8')
	fileHandle.write(result[j])
	fileHandle.write("\n")

