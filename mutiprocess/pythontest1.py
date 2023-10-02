import multiprocessing
import time


def func(msg):
    print("this is "+msg)
    time.sleep(3)
    print("the "+msg+"is end")

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=3)
    for i in range(4):
        msg = f"this is {i}"
        # pool.apply_async(func,(msg,))
        pool.apply(func,(msg,))
    print("-------------------------")
    pool.close()
    pool.join()

