import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
logo = pygame.image.load('pics//logga.png')
screen.blit(logo, (50, 50))
play_sign = pygame.image.load('pics//play_game_logga.png')
screen.blit(play_sign, (250, 250))
quit_sign = pygame.image.load('pics//Quitknapp.png')
screen.blit(quit_sign, (250, 350))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


