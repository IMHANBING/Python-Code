a = [11, 22, 33]
b = a
print(id(a) == id(b))

import copy

c = copy.deepcopy(a)
print(id(a) == id(c))
