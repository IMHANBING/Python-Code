num = 100
num2 = '100'
name = 'lomoo'
print(type(int(num2)))
print(type(str(num)))
print(len(name))
print('姓名：%s' % name)
print('=' * 20)

a = 'lao'
b = 'wang'
c = 'zao'
d = a + b
print(d)
e = a + c
print(e)
A = 100
B = 200
print(type(A + B))
print('=' * 20)

name = 'abcde'
print(name[0])
print(name[2])
print(name[len(name) - 1])
print('=' * 20)

name = 'abcdefABCDEF'
print(name[2:6])
print(name[2:-1])
print(name[2:len(name)])
print(name[2:])
print(name[2:0])
print(name[2::2])
print(name[-1])
print(name[-1::-1])
print('=' * 20)

myStr = 'hello world itcast and itcastxxxcpp'
print(myStr.find('world'))  # 字符串出现位置
print(myStr.find('dog'))  # 字符串不存在：-1
print(myStr.rfind('itcast'))
print(myStr.count('itcast'))  # 字符串出现个数
print(myStr.replace('hello', 'Hello'))
print(myStr.replace('itcast', 'ITCAST', 1))
print(myStr.split(' '))
print(myStr.capitalize())  # 首单词大写
print(myStr.title())  # 每个单词大写
print(myStr.startswith('hello'))
print(myStr.endswith('cpp'))
print('=' * 20)

myStr1 = 'HELLO world itcast and itcastxxxcpp'
print(myStr1.lower())
print(myStr1.upper())
myStr2 = '想陪你一起看大海'
print(myStr2.center(50))
print(myStr2.ljust(50))
print(myStr2.rjust(50))
myStr3 = myStr2.center(50)
print(myStr3.strip())  # 去除字符串内空格
print(myStr3.lstrip())  # 去除字符串内左空格
print(myStr3.rstrip())  # 去除字符串内右空格
print(myStr.partition('itcast'))
print(myStr.rpartition('itcast'))
myStr4 = 'hello\nworld'
print(myStr4.splitlines())
alpha_or_digit = input('输入字母或数字:')
if alpha_or_digit.isalpha():
    print('是字母')
elif alpha_or_digit.isdigit():
    print('是数字')

a = ['aa', 'bb', 'cc']
b = ' '
print(b.join(a))
