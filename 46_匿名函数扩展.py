def test(a, b, func):
    result = func(a, b)
    return result


new_func = eval(input('输入匿名函数'))
num = test(11, 22, new_func)
print(num)
