import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
logo = pygame.image.load('pics//logga.png')
screen.blit(logo, (50, 50))
play_sign = pygame.image.load('pics//play_sign.png')
screen.blit(play_sign, (250, 250))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
