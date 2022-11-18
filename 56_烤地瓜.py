class SweetPotato:
    def __init__(self):
        self.cookedString = '生的'
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return '状态：%s(%d),佐料：%s' % (self.cookedString,
                                        self.cookedLevel,
                                        str(self.condiments))
