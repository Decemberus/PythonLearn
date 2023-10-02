import os


def PrintFileMode(path):
    files = os.listdir(path)
    for name in files:
        pathName = os.path.join(path,name)
        print(pathName)
        mode = os.stat(pathName).st_mode
        print(mode)



PrintFileMode('.')
os.rename("test.txt","test_new.txt")
os.makedirs()
