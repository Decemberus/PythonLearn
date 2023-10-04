import os.path
import socket


class server:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.bufferSize = 9148
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((self.host,self.port))
        s.listen(10)
        print('等待客户端连接')
        while True:
            try:
                conn, addr = s.accept()  # 接收连接
                print('客户端连接 ' + addr[0] + ':' + str(addr[1]))
                while True:  # 保持长连接
                    data = conn.recv(self.bufferSize)  # 接收数据
                    if not data:  # 断开连接时退出当前循环
                        break
                    else:
                        self.executeCommand(conn, data)
                conn.close()  # 关闭当前连接
            except socket.error as e:
                print(e)
                conn.close()  # 关闭连接

    def executeCommand(self,tcpClisock,data):
        try:
            message = data.decode("utf-8")
            if os.path.isfile(message):
                size = str(os.path.getsize(message))
                print(f"the size is {size}")
                #tcpClisock.send(size)之前是这样的，导致一直出错
                tcpClisock.send(size.encode())
                data = tcpClisock.recv(self.bufferSize)
                print("start to send")
                with open(message,"rb") as f:
                    for line in f:
                        tcpClisock.send(line)
            else:
                tcpClisock.send(('0001'+os.popen(message).read()).encode("utf-8"))
        except:
            raise


if __name__ == "__main__":
    s = server("127.0.0.1",8083).start()
