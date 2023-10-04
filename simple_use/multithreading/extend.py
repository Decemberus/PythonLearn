import time
from threading import Thread,current_thread
from typing import Callable, Iterable, Any, Mapping


class MyThread(Thread):

    def __init__(self,id):
        super(MyThread,self).__init__()
        self.id = id
    def run(self):
        time.sleep(5)
        print(self.id)


if __name__ == "__main__":
    t1 = MyThread(999)
    t1.start()
    t1.join()
    for i in range(5):
        print(i)
print("我是主进程")
