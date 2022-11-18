def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


A = (44, 55)
B = {'name': 'laowang'}

test(11, 22, 33, A, B)
print('=' * 20)
test(11, 22, 33, *A, **B)