import pygame
import sys

pygame.init()


def main_menu():
    pygame.mixer.music.load("music//menu_music.ogg")
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((800, 600))

    logo = pygame.image.load('pics//logga.png')
    play_sign = pygame.image.load('pics//play_game_logga.png')
    quit_sign = pygame.image.load('pics//Quitknapp.png')

    play_button = pygame.Rect(250, 250, 300, 100)
    quit_button = pygame.Rect(250, 350, 300, 100)

    pygame.draw.rect(screen, (0, 0, 0), play_button)
    pygame.draw.rect(screen, (0, 0, 0), quit_button)

    screen.blit(play_sign, (250, 250))
    screen.blit(quit_sign, (250, 350))
    screen.blit(logo, (50, 50))


    # running gör så att programmet fortsätter köra för alltid tills running = False
    running = True
    while running:
        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()
            # kollar om det sker knapptryck på musen
            if event.type == pygame.MOUSEBUTTONDOWN:
                #
                mx, my = pygame.mouse.get_pos()
                # kollar vilken knapp på musen som tryckts ned
                if event.button == 1:
                    # kollar om musens position vid knapptryckningen kolliderar med playbutton
                    if play_button.collidepoint(mx, my):
                        # stänger programmet
                        running = False
                    if quit_button.collidepoint(mx, my):
                        sys.exit()

        # uppdaterar displayen
        pygame.display.update()

