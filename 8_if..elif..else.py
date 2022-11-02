yao = input('吃药吗？')
jiu = input('喝酒吗？')
weight = int(input('体重：'))

if yao == '吃' and jiu == '喝' and weight <= 120:
    print('说走就走')
elif (yao == '吃' and jiu == '喝') and weight <= 120:
    print('也许没事')
elif yao == '吃' and jiu == '喝' and not weight <= 120:
    print('胖子无敌')
else:
    print('活得挺好')
