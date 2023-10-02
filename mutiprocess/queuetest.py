import os
import time
from multiprocessing import Process, Queue


def input(q,data):
    q.put(data)
    print(os.getpid())
def out(q):
    time.sleep(5)
    print(q.get())
    print(os.getpid())

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=input,args=(q,[1,23,4]))
    p1.start()
    p1.join()

    p2 = Process(target=out,args=(q,))
    p2.start()
    p2.join()