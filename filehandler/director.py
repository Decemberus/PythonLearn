import os
#
# os.chdir("director")
#
# def ListCurrentDirectory(path):
#     files = os.listdir(path)
#     files_more=os.walk(path)
#     print(files)
#     print(files_more)
#
#
# ListCurrentDirectory(".")


def walkDir(path):
    for dirName, subdirList, fileList in os.walk(path):
        print('发现目录: %s' % dirName)
        # print(subdirList)
        # print(fileList)
        for fname in fileList:
            print('\t%s' % fname)


walkDir('.')