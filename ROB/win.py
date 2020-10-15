import pygame
import sys
from ROB.lobby import lobby

def win():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        lobby()
        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()
            # uppdaterar displayen
        pygame.display.update()
