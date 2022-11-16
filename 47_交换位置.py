a = 4
b = 5

# method1:
c = a
a = b
b = c
print(a, ' ', b)

# method2:
a = a + b
b = a - b
a = a - b
print(a, ' ', b)

# method3:
a, b = b, a
print(a, ' ', b)
