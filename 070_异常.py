try:
    # print(num)
    open('xxx.abc')
    print(111)
except NameError:
    print('名称错误')
except FileNotFoundError:
    print('没有文件')
except Exception:
    print('异常总的父类')