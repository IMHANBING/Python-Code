class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('输入内容：')
        if len(s) < 3:
            raise ShortInputException(len(s),3)
    except ShortInputException as result:
        print('输入长度：%d，至少：%d'%(result.length, result.atleast))
    else:
        print('没有错误')

main()


