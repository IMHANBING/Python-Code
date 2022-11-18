class Animal:
    def eat(self):
        print('eat')


class Dog(Animal):
    def bark(self):
        print('bark')


class FlyDog(Dog):
    def fly(self):
        print('fly')


flyDog = FlyDog()
flyDog.eat()
flyDog.bark()
flyDog.fly()
