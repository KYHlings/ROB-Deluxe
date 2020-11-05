import pygame
import sys

pygame.init()
screen = pygame.display.set_mode(800, 600)
font = pygame.font.SysFont("Arial", 40, True)

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.blit(font.render(f"Press [SPACE] to celebrate", True, (black)), (screen_width/3, 90))