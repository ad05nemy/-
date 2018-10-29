# -*- coding: UTF-8 -*-

import socket
import threading


class Exploit():
    __info__ = {
        "name": "PortScanner",
        "description": "PortScanner",
        "authors": (
            "JSMSF",
        ),
        "references": (
             "www.ggsec.cn "
             "www.secist.com"
        ),

    }


def portscanner(ipadds,port_list):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        t_1=sc.connect_ex((ipadds,port_list))
        if t_1 == 0:
            print('%d  端口开启'%port_list)
            sc.close()
        else:
            print('%d  端口关闭'%port_list)
port_list=[21,22,23,80,139,445,3389,3306]
banner=""" ____            _     _   ____        _       _ _
         / ___|  ___  ___(_)___| |_/ ___| _ __ | | ___ (_) |_
         \___ \ / _ \/ __| / __| __\___ \| '_ \| |/ _ \| | __|
          ___) |  __/ (__| \__ \ |_ ___) | |_) | | (_) | | |_
         |____/ \___|\___|_|___/\__|____/| .__/|_|\___/|_|\__|
           Exploitation Framework for    | |      by JSMSF
                                         |_|



         Codename   : 测试漏洞利用框架
         Version    : 1.0
        """
print(banner)
print('请输入IP或者域名:')
add = input()
try:
    ipadd = socket.gethostbyname(add)
except:
    print('IP地址或者域名错误!')
socket.setdefaulttimeout(2)
portlistlen = range(len(port_list))
print(ipadd)
threads = []
for i in portlistlen:
    t = threading.Thread(target=portscanner, args=(ipadd, port_list[i]))
    threads.append(t)
for i in portlistlen:
    threads[i].start()
for i in portlistlen:
     threads[i].join()