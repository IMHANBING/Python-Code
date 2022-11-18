class Cat:
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return '当前%s在操作'%self.name

    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def introduction(self):
        print('%s的年龄是%d' % (self.name, self.age))


tom = Cat('汤姆',20)
print(tom)
tom.eat()
tom.drink()
tom.introduction()

bluecat = Cat('蓝猫',10)
print(bluecat)
bluecat.introduction()