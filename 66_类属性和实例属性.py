class Tool(object):
    num1 = 0 #类属性
    def __init__(self, new_name):
        self.name = new_name #实例属性
        Tool.num1 += 1

num = 0 #全局属性
tool1 = Tool('铁球')
num += 1
tool2 = Tool('水桶')
num += 1
print(num)