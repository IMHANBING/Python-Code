# 数字，字符串，元组（不可修改）
# 列表，字典（可修改）

nums = [11, 22, 33]
info = {}


def test():
    for num in nums:
        print(num, '', end='')
    nums.append(44)
    info['name'] = 'xiaoming'


def test1():
    print(nums)
    print(info)


test()
print('')
test1()
