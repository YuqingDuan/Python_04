#urlretrieve()
#urlcleanup()
#info()
#getcode() 200 403
#geturl()

import urllib.request
'''
urllib.request.urlretrieve("http://www.hellobi.com", filename="A:/1.html")
urllib.request.urlcleanup()
file=urllib.request.urlopen("http://www.hellobi.com")
print(file.info())
print(file.getcode())
print(file.geturl())
'''

#timeout
file2=urllib.request.urlopen("http://www.hellobi.com", timeout=10)
file3=urllib.request.urlopen("http://www.baidu.com", timeout=1)
for i in range(0,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com", timeout=2)
        data=file.read()
        print(len(data))
    except Exception as ex:
        print("Err: " + str(ex))



        

















