import os

print("second_start")
with open("test.txt","r") as f:
    while True:
        #c = f.read(1)
        #要改成一行行读的话就这样
        c = f.readline()
        if not c:
            break
        print(c)


