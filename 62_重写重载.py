class Animal:
    def eat(self):
        print('eat')


class Dog(Animal):
    def bark(self):
        print('bark')


class FlyDog(Dog):
    def fly(self):
        print('fly')
    def bark(self):
        print('crazy bark')


flyDog = FlyDog()
flyDog.eat()
flyDog.bark()
flyDog.fly()
