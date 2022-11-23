m1 = map(lambda x: x * x, [1, 2, 3])
for temp in m1:
    print(temp, ' ', end='')
print('')

m2 = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
for temp in m2:
    print(temp, ' ', end='')
print('')

from functools import reduce

r1 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(r1)

r2 = reduce(lambda x, y: x + y, [1, 2, 3, 4], 5)
print(r2)

s1 = [3, 4, 2, 1]
print(sorted(s1))
print(sorted(s1, reverse=1))
