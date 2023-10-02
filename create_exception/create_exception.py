class ShortInputException(Exception):
    def __int__(self,len,atlest):
        self.len=len
        self.atlest=atlest
try:
    s=input('input :')
    if len(s) < 3:
        raise ShortInputException(len(s),3)
except EOFError:
    print("no eof")
except ShortInputException as x:
    print(x.len,x.atlest)
else:
    print("catch any exception")

