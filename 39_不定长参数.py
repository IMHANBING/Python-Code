def sum_2_nums(a, b, *args):
    print(a)
    print(b)
    print(args)  # tuple
    result = a + b
    for num in args:
        result += num
    print(result)


sum_2_nums(11, 22, 33, 44, 55)
