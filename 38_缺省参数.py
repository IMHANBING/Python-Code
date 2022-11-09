def test(a, b=22):
    print(a + b)


test(11)
test(11, 33)


def test1(a, b=22, c=33):
    print(a + b + c)


test1(11, c=44)
