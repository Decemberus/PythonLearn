# import socket
# import sys
#
#
# class server:
#     def __init__(self,host,port):
#         self.host = host
#         self.port = port
#     def start(self):
#         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         try:
#             s.bind((self.host,self.port))
#             s.listen(10)
#             print("waiting for connect")
#             conn,address = s.accept()
#             data = conn.recv(4096)
#             print(f"客户端数据{data}")
#             conn.sendall("hello client")
#             conn.close()
#         except:
#             print("error")
#             sys.exit()
#         finally :
#             s.close()
# if __name__ == "__main__":
#     server("192.168.3.149",2777).start()

# -*- coding: UTF-8 -*-

import socket
import sys


class server:
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket
        try:
            s.bind((self.ip, self.port))  # 绑定
            s.listen(10)  # 监听
            print('等待客户端连接')
            conn, addr = s.accept()  # 接收连接
            print('客户端连接 ' + addr[0] + ':' + str(addr[1]))
            data = conn.recv(1024)  # 接收数据
            print("客户端数据：%s" % data)
            conn.sendall(bytes("你好客户端\n\r", encoding="utf8"))  # 发送数据
            conn.close()  # 关闭连接

        except socket.error as e:
            print(e)
            sys.exit()
        finally:
            s.close()  # 关闭服务端


if __name__ == '__main__':
    s = server('127.0.0.1', 8800)
    s.start()

