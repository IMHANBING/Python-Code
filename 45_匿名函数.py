info = [{'name': 'laowang', 'age': 30},
        {'name': 'xiaoming', 'age': 21},
        {'name': 'banzhang', 'age': 12}]
info.sort(key=lambda x: x['name'])
print(info)
info.sort(key=lambda x: x['age'])
print(info)
