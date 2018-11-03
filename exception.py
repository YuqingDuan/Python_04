#父URLError
#子HTTPError
#两者都是异常处理的类，HTTPError是URLError的子类，HTTPError有异常状态码与异常原因，URLError没有异常状态码。
#所以在处理的时候，不能使用URLError直接代替HTTPError。如果要代替，必须要判断是否有状态码属性。
'''
URLError：
1.连不上服务器
2.远程的url不存在
3.本地没有联网
4.触发了子类HTTPError
'''

import urllib.error
import urllib.request

try:
    urllib.request.urlopen("http://www.udemy.com/nodejs-the-complete-guide/")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
