import pygame
import numpy as np


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 600
        self.image = pygame.image.load('./feiji/hero1.png')
        self.screen = screen_temp
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x + 40, self.y - 12))


class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load('./feiji/enemy0.png')
        self.Rex_temp = 0
        self.Rey_temp = 0
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def newThread(self):
        self.Rex_temp = np.random.randint(-1, 2)  # (-1, 0, 1)
        self.Rey_temp = np.random.randint(-1, 2)

    def move(self):
        if self.Rex_temp > 0 and self.Rey_temp > 0:
            self.x += 2
            self.y += 2
        elif self.Rex_temp > 0 and self.Rey_temp == 0:
            self.x += 2
        elif self.Rex_temp > 0 and self.Rey_temp < 0:
            self.x += 2
            self.y -= 2
        elif self.Rex_temp == 0 and self.Rey_temp > 0:
            self.y += 2
        elif self.Rex_temp == 0 and self.Rey_temp < 0:
            self.y -= 2
        elif self.Rex_temp < 0 and self.Rey_temp > 0:
            self.x -= 2
            self.y += 2
        elif self.Rex_temp < 0 and self.Rey_temp == 0:
            self.x -= 2
        elif self.Rex_temp < 0 and self.Rey_temp < 0:
            self.x -= 2
            self.y -= 2
        if self.x < 0:
            self.x = 0
        elif self.x + 100 > 480:
            self.x = 480 - 100
        elif self.y < 0:
            self.y = 0
        elif self.y + 124 > 750:
            self.y = 750 - 124

    def fire(self):
        if np.random.randint(501) > 495:
            self.bullet_list.append(EnemyBullet(self.screen, self.x + 22, self.y + 40))


class EnemyBullet(object):
    def __init__(self, screen_temp, x_temp, y_temp):
        self.x = x_temp
        self.y = y_temp
        self.image = pygame.image.load('./feiji/bullet1.png')
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 2

    def judge(self):
        if self.y > 750:
            return True
        else:
            return False


class Bullet(object):
    def __init__(self, screen_temp, x_temp, y_temp):
        self.x = x_temp
        self.y = y_temp
        self.image = pygame.image.load('./feiji/bullet.png')
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hero_temp.move_left()
            elif event.key == pygame.K_d:
                hero_temp.move_right()
            elif event.key == pygame.K_w:
                hero_temp.move_up()
            elif event.key == pygame.K_s:
                hero_temp.move_down()
            elif event.key == pygame.K_j:
                hero_temp.fire()


def main():
    pygame.init()
    screen = pygame.display.set_mode([480, 750], False, 32)
    background = pygame.image.load('./feiji/background.png')
    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.newThread()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)


if __name__ == '__main__':
    main()
