class SweetPotato:
    def __init__(self):
        self.cookedString = '生的'
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return '状态：%s(%d),佐料：%s' % (self.cookedString,
                                        self.cookedLevel,
                                        str(self.condiments))

    def cook(self, cookedTime):
        self.cookedLevel += cookedTime
        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = '生的'
        elif self.cookedLevel >= 3 and self.cookedLevel < 5:
            self.cookedString = '半生不熟'
        elif self.cookedLevel >= 5 and self.cookedLevel < 8:
            self.cookedString = '熟了'
        elif self.cookedLevel >= 8:
            self.cookedString = '糊了'

    def addCondiments(self, item):
        self.condiments.append(item)


sp = SweetPotato()
print(sp)
sp.cook(3)
sp.addCondiments('红糖')
print(sp)
sp.cook(2)
sp.addCondiments('蜂蜜')
print(sp)
sp.cook(3)
print(sp)
