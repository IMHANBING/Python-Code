import pygame


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 600
        self.image = pygame.image.load('feiji/hero1.png')
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5


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


def main():
    pygame.init()
    screen = pygame.display.set_mode([480, 750], False, 32)
    background = pygame.image.load('feiji/background.png')
    hero = HeroPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()
        key_control(hero)


if __name__ == '__main__':
    main()
