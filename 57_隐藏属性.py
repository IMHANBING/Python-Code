class Dog:
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.__age = new_age

    def __str__(self):
        return '%s的年龄是：%d' % (self.name, self.__age)

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        if new_age >= 0 and new_age <= 100:
            self.__age = new_age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age


dog = Dog('小白', 10)
print(dog)
dog.set_name('小黑')
dog.set_age(-10)
print(dog)
