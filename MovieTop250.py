import requests
from lxml import etree
import time
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36"
						 "(KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
for i in range(10):
	url = 'https://movie.douban.com/top250?start=' + str(i * 25)
	response = requests.get(url, headers=headers)#抓取页面
	html = etree.HTML(response.text) #调用HTML类进行初始化，构造XPath解析对象
	lists = html.xpath("//ol[@class='grid_view']/li")# 获取25个li节点，节点里包含电影信息
	for item in lists: #遍历lists
		#获取电影信息
		link = item.xpath("div//div[2]//div[@class='hd']//@href")[0] #电影链接
		title = item.xpath("div//div[2]//div[@class='hd']//a//span[1]//text()")[0] #电影名
		rating = item.xpath("div//div[2]//div[@class='star']//span[2]//text()")[0] #评分
		evaluate_num = item.xpath("div//div[2]//div[@class='star']//span[4]//text()")[0] #评价人数
		overview = item.xpath("div//div[2]//div[@class='bd']//p[1]//text()") #导演/主演/年份/地区/类型
		ranking = item.xpath("div//div[@class='pic']//em//text()")[0] #电影排名
		#引言，有些电影没有引言，所以添加异常处理
		try:
			inq = item.xpath("div//div[2]//div[@class='bd']//p[@class='quote']//span//text()")[0].strip() 
		except IndexError:
			inq = 'no'
		#处理、整合电影信息
		movie = 'No.' + ranking + '.' + title + ' ' + link  + ' ' + overview[0].strip() \
				+ '\n' + overview[1].strip() + ' ' + rating + ' ' + evaluate_num\
				+ ' ' + inq + '\n'
		time.sleep(1) #延时等待
		print(movie) #输出爬取的电影信息
		#把电影信息写入文件
		with open('MoveTop250.txt', 'a', encoding='utf-8') as f:
			f.write(movie + '\n')


