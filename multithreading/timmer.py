import threading


class timer:
    def hello(self):
        print("hello timer")

if __name__ == '__main__':
    t1=threading.Timer(3.0,timer().hello)
    t1.start()