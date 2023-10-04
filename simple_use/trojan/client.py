import os
import re
import socket
import sys


class client:
    def __init__(self,server_ip,server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.bufferSize = 9048

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((self.server_ip,self.server_port))
            while True:
                message = input("> ")
                if not message:
                    break
                s.send(bytes(message,'utf-8'))
                data = s.recv(self.bufferSize)
                if not data:
                    break
                if re.search("^0001",data.decode('utf-8',"ignore")):
                    print(data.decode('utf-8'))
                else:
                    s.send("start to send the file".encode())
                    file_size = int(data.decode())
                    with open("new" +os.path.split(message)[-1], "wb") as f:         #创建文件
                        receive_size = 0
                        while receive_size < file_size:
                            data = s.recv(self.bufferSize)
                            f.write(data)
                            receive_size += file_size

                            print(f"already recieve {data}")
                        f.close()
                        print("receive done", file_size, " ", receive_size)

        except socket.error as e:
            s.close()
            print(f"socket is error because of {e}")
            raise
        finally:
            s.close()

if __name__ == '__main__':
    cl = client('127.0.0.1',8083)
    cl.connect()
    sys.exit() #退出进程
