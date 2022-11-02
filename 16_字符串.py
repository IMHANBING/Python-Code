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
