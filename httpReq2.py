#自动模拟HTTP请求（post）
#验证地址 http://www.iqianyue.com/mypost/
import urllib.request
import urllib.parse

#表单提交实际路径
url="http://www.iqianyue.com/mypost/"
#编辑表单提交的内容
mydata=urllib.parse.urlencode(
        {"name":"test@qq.com",
         "pass":"123456"
            }
    ).encode("utf-8")
#将url和表单内容封装成post请求
req=urllib.request.Request(url, mydata)
#发送请求，获得数据
data=urllib.request.urlopen(req).read()
#将得到的数据保存到本地
handle=open("A:/3.html", "wb")
handle.write(data)
handle.close()
