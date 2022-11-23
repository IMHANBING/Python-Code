class Person(object):
    def __init__(self, new_name):
        super(Person, self).__init__()
        self.name = new_name
        self.gun = None
        self.hp = 100

    def clip_and_missile(self, clip_temp, missile_temp):
        clip_temp.save(missile_temp)

    def gun_and_clip(self, gun_temp, clip_temp):
        gun_temp.save(clip_temp)

    def take(self, gun_temp):
        self.gun = gun_temp

    def __str__(self):
        if self.gun:
            return '%s的血量是：%d，他有枪，%s' % (self.name, self.hp, self.gun)
        else:
            return '%s的血量是：%d，他没有枪' % (self.name, self.hp)

    def shot(self, enemy_temp):
        self.gun.fire(enemy_temp)

    def losshp(self, killability_temp):
        self.hp -= killability_temp


class Gun(object):
    def __init__(self, new_name):
        super(Gun, self).__init__()
        self.name = new_name
        self.clip = None

    def save(self, clip_temp):
        self.clip = clip_temp

    def __str__(self):
        if self.clip:
            return '枪的型号：%s, %s' % (self.name, self.clip)
        else:
            return '枪的型号：%s, 目前没有子弹' % self.name

    def fire(self, enemy_temp):
        missile_temp = self.clip.lossmissile()
        if missile_temp:
            missile_temp.kill(enemy_temp)
        else:
            print('快装弹，没有子弹了')

class Clip(object):
    def __init__(self, num):
        super(Clip, self).__init__()
        self.max_num = num
        self.missile_list = []

    def save(self, missile_temp):
        self.missile_list.append(missile_temp)

    def __str__(self):
        return '弹夹数量：%s / %s' % (len(self.missile_list), self.max_num)

    def lossmissile(self):
        if self.missile_list:
            return self.missile_list.pop()
        else:
            return None

class Missile(object):
    def __init__(self, ability):
        super(Missile, self).__init__()
        self.killability = ability

    def kill(self, enemy_temp):
        enemy_temp.losshp(self.killability)

def main():
    laowang = Person('老王')
    ak47 = Gun('ak47')
    clip = Clip(30)
    for i in range(30):
        missile = Missile(10)
        laowang.clip_and_missile(clip,missile)
    laowang.gun_and_clip(ak47,clip)
    print(clip)
    print(ak47)
    laowang.take(ak47)
    print(laowang)
    enemy = Person('老李')
    print(enemy)
    laowang.shot(enemy)
    laowang.shot(enemy)
    laowang.shot(enemy)
    print(enemy)
    print(laowang)


main()