import multiprocessing
import os, time, random

def Lee():
    print("\nRun task Lee-%s" %(os.getpid())) #os.getpid()获取当前的进程的ID
    start = time.time()
    time.sleep(random.random() * 10) #random.random()随机生成0-1之间的小数
    end = time.time()
    print('Task Lee, runs %0.2f seconds.' %(end - start))

def Marlon():
    print("\nRun task Marlon-%s" %(os.getpid()))
    start = time.time()
    time.sleep(random.random() * 40)
    end=time.time()
    print('Task Marlon runs %0.2f seconds.' %(end - start))

def Allen():
    print("\nRun task Allen-%s" %(os.getpid()))
    start = time.time()
    time.sleep(random.random() * 30)
    end = time.time()
    print('Task Allen runs %0.2f seconds.' %(end - start))

def Frank():
    print("\nRun task Frank-%s" %(os.getpid()))
    start = time.time()
    time.sleep(random.random() * 20)
    end = time.time()
    print('Task Frank runs %0.2f seconds.' %(end - start))

if __name__ == "__main__":
    list = [Lee,Marlon,Allen,Frank]
    pool = multiprocessing.Pool(4)
    for i in list:
        pool.apply_async(func=i)

    print("wait for subprocess")
    pool.close()
    pool.join()
    print("all process are done ")

