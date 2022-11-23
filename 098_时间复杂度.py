import time

start_time = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)
end_time = time.time()
print(end_time - start_time)
# 1<logn<n<nlogn<n^2<n^3<2^n<n!<n^n
