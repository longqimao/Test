import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
				 '(KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.explore-feed.feed-item').items()
for item in items:
	question = item.find('h2').text()
	author = item.find('author-link-line').text()
	answer = pq(item.find('.content').html()).text()

	# file = open('explore.txt', 'a', encoding='utf-8')
	# file.write('\n'.join([question, author, answer]))
	# file.write('\n' + '=' *50 + '\n')
	# file.close()

	with open('explore.txt', 'a', encoding='utf-8') as file:
		file.write('\n'.join([question, author, answer]))
		file.write('\n' + '=' *50 + '\n')









