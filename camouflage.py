#爬虫的浏览器伪装技术
#User-Agent
#urllib.request.build_opener()添加报头信息
#https://www.udemy.com/nodejs-the-complete-guide/
#http://blog.csdn.net/weiwei_pig/article/details/52123738
import urllib.request

#需要访问的地址
url="http://www.udemy.com/nodejs-the-complete-guide/"
#浏览器伪装
headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
#添加报头信息
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#获取网站数据
data=opener.open(url).read()
#将网页资源保存到你本地
fh=open("A:/4.html","wb")
fh.write(data)
fh.close()
