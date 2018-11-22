import requests
from lxml import etree
import time
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36"
						 "(KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
for i in range(10):
	url = 'https://movie.douban.com/top250?start=' + str(i * 25)
	response = requests.get(url, headers=headers)
	html = etree.HTML(response.text)
	lists = html.xpath("//ol[@class='grid_view']/li")
	for item in lists:
		link = item.xpath("div//div[2]//div[@class='hd']//@href")[0]
		title = item.xpath("div//div[2]//div[@class='hd']//a//span[1]//text()")[0]
		rating = item.xpath("div//div[2]//div[@class='star']//span[2]//text()")[0]
		evaluate_num = item.xpath("div//div[2]//div[@class='star']//span[4]//text()")[0]
		overview = item.xpath("div//div[2]//div[@class='bd']//p[1]//text()")
		ranking = item.xpath("div//div[@class='pic']//em//text()")[0]
		try:
			inq = item.xpath("div//div[2]//div[@class='bd']//p[@class='quote']//span//text()")[0].strip()
		except IndexError:
			inq = 'no'
		movie = 'No.' + ranking + '.' + title + ' ' + link  + ' ' + overview[0].strip() \
				+ '\n' + overview[1].strip() + ' ' + rating + ' ' + evaluate_num\
				+ ' ' + inq + '\n'
		time.sleep(1)
		print(movie)
		# with open('MoveTop250.txt', 'a', encoding='utf-8') as f:
		# 	f.write(movie + '\n')


