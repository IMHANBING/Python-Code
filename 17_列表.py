print('定义列表')
nums = [11, 3.14, '老王']
print(type(nums))
print('列表增操作')
names = ['老王', '老李', '老赵']
names.append('老刘')
print(names)
names.insert(4, '老孙')
print(names)

names2 = ['葫芦娃', '白骨精']
names.extend(names2)
print(names)

print('列表删操作')
names.pop()
print(names)
names.remove('葫芦娃')
print(names)
del names[-1]   # 删除
print(names)

print('列表改操作')
names[-1] = '老钱'
print(names)

print('列表查操作')
if '老赵' in names:
    print('找到了')
elif '老赵' not in names:
    print('没有')
