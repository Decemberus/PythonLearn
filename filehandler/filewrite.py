filePath = './test.txt'
def printContent(path):
    with open(path,'r') as f:
        print(f.read())

def writeContent(path):
    with open(path,'a') as f:
        f.writelines("\nwrite")

printContent(filePath)
writeContent(filePath)

