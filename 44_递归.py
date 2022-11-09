i = 1
result = 1
while i < 5:
    result *= i
    i += 1
print(result)


def get_num(num):
    if num > 1:
        return num * get_num(num - 1)
    else:
        return num


print(get_num(4))
