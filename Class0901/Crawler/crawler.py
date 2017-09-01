import requests
from bs4 import BeautifulSoup
import lxml

res = requests.get('http://www.comm.yzu.edu.tw/')
content = res.text.encode('utf-8')
soup = BeautifulSoup(content, "lxml")
all_urls = map(lambda x: x['href'], soup.find_all('a', href=True))

# print soup.find('title').string

print len(all_urls)
print len(set(all_urls))
print set(all_urls)
