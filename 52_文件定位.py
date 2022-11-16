f = open('01_hello.py','r')
f.seek(2,0)
print(f.readline())
print(f.tell())