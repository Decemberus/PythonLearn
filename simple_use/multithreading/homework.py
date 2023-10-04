import os
import threading


dirlist = ["./","../","C:/Users/enjoy/Desktop/usage"]
threads= []
def walkdir(path):
    print(f"当前线程：{threading.current_thread().name}")
    for dirName,subdirList,fileList in os.walk(path):
        print(f"发现目录：{dirName}")
        for fname in fileList:
            print("\t"+ fname)
if __name__ == '__main__':
    for director in dirlist:
        t = threading.Thread(target=walkdir,args=(director,))
        threads.append(t)
        t.start()

#wonderful