class Dog(object):
    def print_self(self):
        print('hello world')


class LittleDog(Dog):
    def print_self(self):
        print('nothing, never mind')


def introduce(temp):
    temp.print_self()


dog = Dog()
dog.print_self()
littleDog = LittleDog()
littleDog.print_self()

introduce(dog)
introduce(littleDog)
