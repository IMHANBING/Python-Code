class Person(object):
    num = 0
    print('person test')

    def __init__(self):
        self.name = 'abc'


print(Person)


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            print('class Foo')

        return Foo
    else:
        class Bar(object):
            print('class Bar')

        return Bar


MyClass = choose_class('foo')
print(MyClass)


class Animal(object):
    def eat(self):
        print('eat')


class Dog(Animal):
    pass


dog = Dog()
dog.eat()
Cat = type('Cat', (Animal, ), {'name':'lili'})
cat = Cat()
cat.eat()
print(cat.name)
print(Cat.__class__)
