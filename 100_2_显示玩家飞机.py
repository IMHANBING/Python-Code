import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode([480, 750], False, 32)
    background = pygame.image.load('feiji/background.png')
    hero = pygame.image.load('feiji/hero1.png')
    x = 200
    y = 600
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x -= 5
                elif event.key == pygame.K_d:
                    x += 5
                elif event.key == pygame.K_w:
                    y -= 5
                elif event.key == pygame.K_s:
                    y += 5


if __name__ == '__main__':
    main()
