a = [x for x in range(10)]
print(a)

b = (x for x in range(10))
print(b)
for temp in range(10):
    print(next(b), ' ', end='')

print('')


def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        print(b, ' ', end='')
        a, b = b, a + b
        yield n
    return 'done'


f = fib(10)
for temp in range(10):
    next(f)
