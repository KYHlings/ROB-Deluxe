import pygame
import sys
from ROB.main_menu import main_menu


screen = pygame.display.set_mode((800, 600))


def main():
    running = True
    while running:

        main_menu()
        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()


main()


