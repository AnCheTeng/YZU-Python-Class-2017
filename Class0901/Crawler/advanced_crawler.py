import requests
import time
from bs4 import BeautifulSoup
import lxml

def craw_one_page(url):
    res = requests.get(url)
    content = res.text.encode('utf-8')
    soup = BeautifulSoup(content, "lxml")
    urls_inpage = map(lambda x: x['href'], soup.find_all('a', href=True))
    return urls_inpage

def write_to_file(url, filename):
    res = requests.get(url)
    content = res.text.encode('utf-8')
    with open(filename, "w") as f:
        f.write(content)

target = 'http://www.comm.yzu.edu.tw/'
all_pages = set(craw_one_page(target))

i = 0
for each_url in all_pages:
    time.sleep(1)
    print "Fetch: " + each_url
    try:
        write_to_file(each_url, "page-"+str(i)+".html")
        print "------> Successful fetch: " + each_url
        i += 1
    except:
        print "------> Failed to fetch: " + each_url
