#自动模拟HTTP请求（get）
import urllib.request

keyword="Python"
#关键词中文编码处理
kw=urllib.request.quote(keyword)
#组织请求的url
url="http://www.baidu.com/s?wd="+kw
#将组织好的url封装成get请求模式
req=urllib.request.Request(url)
#发送请求，获得数据
data=urllib.request.urlopen(req).read()
#将得到的数据保存到本地
handle=open("A:/2.html", "wb")
handle.write(data)
handle.close()
