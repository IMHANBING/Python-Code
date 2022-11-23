info = [{'name': 'lao wang', 'age': 30},
        {'name': 'xiao ming', 'age': 21},
        {'name': 'ban zhang', 'age': 12}]
info.sort(key=lambda x: x['name'])
print(info)
info.sort(key=lambda x: x['age'])
print(info)
