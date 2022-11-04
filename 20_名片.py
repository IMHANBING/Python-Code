print('1:增加')
print('2:删除')
print('3:修改')
print('4:查询')
print('=' * 20)
infos = []
while True:
    num = int(input('输入序号：'))
    if num == 1:
        new_name = input('输入姓名：')
        new_addr = input('输入地址：')
        new_age = int(input('输入年龄：'))
        new_info = {}
        new_info['name'] = new_name
        new_info['addr'] = new_addr
        new_info['age'] = new_age
        infos.append(new_info)
        print(infos)
    elif num == 2:
        del_name = input('输入姓名：')
        del_flag = 0
        for temp in infos:
            if temp['name'] == del_name:
                infos.remove(temp)
                print(infos)
                del_flag = 1
                break
        if del_flag == 0:
            print('没有此人')
    elif num == 3:
        upd_name = input('输入姓名：')
        upd_info = input('修改内容：')
        upd_flag = 0
        for temp in infos:
            if temp['name'] == upd_name:
                upd_item = input('输入哪一项：')
                if upd_item == 'name':
                    temp['name'] = upd_info
                elif upd_item == 'addr':
                    temp['addr'] = upd_info
                elif upd_item == 'age':
                    temp['age'] = int(upd_info)
            print(infos)
            upd_flag = 1
            break
        if upd_flag == 0:
            print('没有此人')
    elif num == 4:
        print('姓名\t地址\t年龄\t\n')
        for temp in infos:
            print('%s\t%s\t%d' % (temp['name'], temp['addr'], temp['age']))
    elif num == 5:
        pass
    elif num == 6:
        break
    else:
        print('输入有误')
