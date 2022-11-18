class Animal(object):
    def eat(self):
        print('eat')

    def drink(self):
        pass


class Dog(Animal):
    def bark(self):
        print('bark')


class Cat(Animal):
    pass


a = Animal()
a.eat()
dog = Dog()
dog.eat()
dog.bark()
cat = Cat()
cat.eat()
