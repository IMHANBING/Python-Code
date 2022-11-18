a = []
i = 1
while i <= 100:
    a.append(i)
    i += 1
print(a)

b = []
for j in range(100):
    j += 1
    b.append(j)
print(b)

c = [i for i in range(100) if i % 2 != 0]
print(c)

d = [(i, j) for i in range(3) for j in range(2)]
print(d)
