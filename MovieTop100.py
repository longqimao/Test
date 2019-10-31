import requests
from lxml import etree
import time
def get_movie():
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
					  '(KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
	}
	url = 'http://maoyan.com/board/4?offset=' + str(i*10)
	response = requests.get(url, headers=headers).text
	html = etree.HTML(response)
	lists = html.xpath('//dd')
	for item in lists:
		index = item.xpath('i//text()')[0]
		info = item.xpath('div[@class="board-item-main"]//p//text()')
		score = item.xpath('div//p[@class="score"]//text()')
		content = "".join(score)
		movie = index + '.' + info[0] + ' ' + info[1].\
			strip() + ' ' + info[2] + ' 评分: ' + content + '\n'
		print(movie)
		with open('TOP100.txt', 'a', encoding='utf-8') as f:
			f.write(movie + '\n')
		time.sleep(1)
for i in range(10):
	get_movie()

