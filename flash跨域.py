# -*- coding: UTF-8 -*-
import re
import requests
import os
import os.path
import threading
import time

headers={'Accept':'*/*',
         'Accept-Language':'en',
         'User-Agent':'Mozilla/5.0 (compatible; Windows NT 6.1; Trident/5.0)',
         'Connection':'close',
         'Referer':'https://www.taobao.com'}
def xmlscanner(url):
        try:
            respose=requests.get('http://'+url+'/crossdomain.xml',headers=headers,timeout=5)
        except:
            print (url+'连接失败')
            return
        s=requests.session()
        s.keep_alive=False
        print ('\n\n'+url)
        print('状态码:'+str(respose.status_code))
        END = respose.content
        if ('domain="*"').encode('utf-8') in END.lstrip():
            print ('存在flash跨域')
            fileHandle=open('test.txt','a')
            fileHandle.write(url+'/crossdomain.xml'+'\n\n')
            fileHandle.close()

domains=[]
url=open('url.txt','r+')
urllist=url.readlines()
for line in range(len(urllist)):
    urllist[line]=urllist[line].strip()
url.close()
domainslen=range(len(urllist))
threads = []
for i in domainslen:
    t = threading.Thread(target=xmlscanner, args=(urllist[i],))
    threads.append(t)
for i in domainslen:
    threads[i].start()
for i in domainslen:
     threads[i].join()
