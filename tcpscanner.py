# -*- coding: UTF-8 -*-

import socket
from secistsploit.core.exploit import *
from secistsploit.core.tcp.tcp_scanner import tcpscanner


class Exploit(tcpscanner):
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

def scanner(adds,ports):
    try:
        ipadd=socket.gethostbyname(adds)
    except:
        print('IP地址或者域名错误!')
    socket.setdefaulttimeout(2)
    for port_list in ports:
        print('正在扫描IP  '+ipadd+':'+str(port_list))
        portscanner(ipadd,port_list)
def portscanner(ipadd,port_list):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        t_1=sc.connect_ex((ipadd,port_list))
        if t_1 == 0:
            print('%d  端口开启'%port_list)
            print('----------------------')
            sc.close()
        else:
            print('%d  端口关闭'%port_list)
            print('----------------------')
port_list=[21,22,23,80,139,445,1433,3389,3306]
print('请输入IP或者域名:')
add = input()
scanner(add,port_list)