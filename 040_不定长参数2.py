def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


test(11, 22, 33, 44, 55, task=66, done=55)
