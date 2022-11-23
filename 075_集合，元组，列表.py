a = (11, 11, 22)
print(a, type(a))

b = [11, 11, 22]
print(b, type(b))

c = {11, 11, 22}
print(c, type(c))

d = [11, 11, 22]
e = []
for i in d:
    if i not in e:
        e.append(i)
print(e)

f = set(a)
g = list(f)
print(g)
