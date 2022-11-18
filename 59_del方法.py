class Dog:
    def __str__(self):
        return 'object exit'

    def __del__(self):
        print('对象删除')

dog1 = Dog()
dog2 = dog1

del dog1

print(dog2)