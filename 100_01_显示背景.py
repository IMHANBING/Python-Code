import pygame

def main():
    pygame.init()
    screen=pygame.display.set_mode([480, 750], False, 32)
    background=pygame.image.load('./feiji/background.png')
    screen.blit(background, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

if __name__=='__main__':
    main()