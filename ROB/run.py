import pygame
import sys
from ROB.main_menu import main_menu
# TODO - Ändra så att man använder klasser som screen states

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        main_menu()
        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()
            # uppdaterar displayen
        pygame.display.update()


if __name__ == '__main__':
    main()