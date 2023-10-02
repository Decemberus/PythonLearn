import socket
import sys

class Client:
    def __init__(self,host):
        self.host = host
    def connect(self):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # except socket.error as e:
        #     print(f"wrong {e}")
        #     sys.exit()
        #
        # try:
        #     remote_ip = socket.gethostbyname(self.host)
        # except socket.gaierror:
        #     print("cant resolve the id")
        #     sys.exit()
        # try:
            s.connect((self.host,8800))
            message = b"GET / HTTP/1.1\r\n\r\n"
            s.sendall(message)
            reply = s.recv(4096)
            print(reply)
            s.close()
        except socket.error:
            sys.exit()


if __name__ == "__main__":
    Client("127.0.0.1").connect()



