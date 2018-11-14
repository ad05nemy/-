import socket
import threading

def recv_datas():
    while True:
        recv_data=str(conn.recvfrom(1024),encoding="utf-8")
        print('\n'+'Other:'+recv_data+'\n'+'Me:')
def send_datas():
    while True:
        send_data=input()
        conn.sendall(bytes(send_data,encoding='utf-8'))
        if send_data=='exit':break
ip_port=('127.0.0.1',8080)
sc = socket.socket()
sc.bind(ip_port)
sc.listen(5)
conn, address = sc.accept()
conn.sendall(bytes("Hello", encoding="utf-8"))
threads = []
t1=threading.Thread(target=recv_datas)
threads.append(t1)
t2=threading.Thread(target=send_datas)
threads.append(t2)
for t in threads:
    t.setDaemon(True)
    t.start()
t.join()