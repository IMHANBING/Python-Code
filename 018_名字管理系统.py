print('1: 新增')
print('2: 删除')
print('3: 修改')
print('4: 查询')
print('=' * 20)
names = []
while True:
    num = int(input('输入序号：'))
    if num == 1:
        ins_name = input('输入姓名：')
        names.append(ins_name)
        print(names)
    elif num == 2:
        del_name = input('输入姓名：')
        names.remove(del_name)
        print(names)
    elif num == 3:
        upd_name = input('输入姓名：')
        upd_p = int(input('输入位置：'))
        names[upd_p] = upd_name
        print(names)
    elif num == 4:
        sel_p = int(input('输入位置：'))
        print(names[sel_p])
    elif num == 5:
        break
    else:
        print('输入有误')
