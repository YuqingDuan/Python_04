#制作一个简单的爬虫爬取sina新闻首页的所有内容到本地
import urllib.request
import re
import urllib.error

url="http://news.sina.com.cn"
data=urllib.request.urlopen(url).read()
data=data.decode("utf-8", "ignore")
regex='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(regex).findall(data)

for i in range(0, len(allurl)):
    try:
        print("The" + str(i) +"-th: ")
        thisurl=allurl[i]
        filename="A:/sinanews" + str(i) + ".html"
        urllib.request.urlretrieve(thisurl, filename)
        print("----------success----------")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

