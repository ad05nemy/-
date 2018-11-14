import socket
import threading


def recv_datas():
    while True:
        ret = str(obj.recv(1024), encoding="utf-8")
        print('Other:' + ret+'\n'+'Me:')


def send_datas():
    while True:
        send_data = input()
        if send_data == 'exit': break
        if send_data == '/help':
            print('exit     退出')
        else:
            obj.sendall(bytes(send_data, encoding='utf-8'))

obj = socket.socket()
obj.connect_ex(("127.0.0.1", 8080))
print('输入/help 查看帮助')
threads = []
t1=threading.Thread(target=recv_datas)
threads.append(t1)
t2=threading.Thread(target=send_datas)
threads.append(t2)
for t in threads:
    t.setDaemon(True)
    t.start()
t.join()
