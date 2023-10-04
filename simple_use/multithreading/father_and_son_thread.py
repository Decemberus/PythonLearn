from threading import Thread,current_thread

class MyThread(Thread):

    def __init__(self,n):
        if n != "":
            super(MyThread,self).__init__(name = n)

        else:
            super(MyThread, self).__init__()
    def run(self):
        print("task",self.name)


t1 = MyThread("")
t2 = MyThread("")
t1.start()

t2.start()
