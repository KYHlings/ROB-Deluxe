import pygame
import sys

pygame.init()

font = pygame.font.SysFont("Arial", 40, True)
font2 = pygame.font.SysFont("Arial", 25)
black = (0, 0, 0)
gold = (207, 181, 59)
white = (255, 255, 255)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = pygame.image.load('images/backgrounds/dice_bg.jpg')
# player1 = pygame.image.load('images/sprites/sune/walking_right_0.png')
# player2 = pygame.image.load('images/sprites/bob/walking_right_green_0.png')
# player3 = pygame.image.load('images/sprites/berit/walking_right_yellow_0.png')
# player4 = pygame.image.load('images/sprites/hannes/walking_right_purple_0.png')

player1_l = pygame.image.load('images/sprites/sune/red_hit.png')
player1_l = pygame.transform.scale(player1_l, (400, 350))
player2_l = pygame.image.load('images/sprites/bob/green_hit.png')
player2_l = pygame.transform.scale(player2_l, (400, 350))
player3_l = pygame.image.load('images/sprites/berit/yellow_hit.png')
player3_l = pygame.transform.scale(player3_l, (400, 350))
player4_l = pygame.image.load('images/sprites/hannes/blue_hit.png')
player4_l = pygame.transform.scale(player4_l, (400, 350))

matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"],
           ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"],
           ["Boxare Bob", "Bråkiga Berit"]]
podium = pygame.image.load('images/gui/podium.png')


def end_screen(first, second, third, fourth):
    running = True
    while running:
        screen.blit(bg_image, (0, 0))
        screen.blit(podium, (700, 450))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_p:
                    main_main_window()
                    return

        if first > second and first > third and first > fourth:
            screen.blit(font.render(f"Winner is: Slaktar Sune", True, gold), (100, 150))
            screen.blit(font.render("Oh Yeah!!", True, gold), (505, 425))
            screen.blit(player1_l, (510, 435))
        # screen.blit(player4, (550, 500))
        # screen.blit(player2, (500, 500))
        # screen.blit(player3, (450, 500))
        elif second > first and second > third and second > fourth:
            screen.blit(font.render(f"Winner is: Boxare Bob", True, gold), (100, 150))
            screen.blit(font.render("Oh Yeah!!", True, gold), (505, 425))
            screen.blit(player2_l, (510, 435))
        # screen.blit(player1, (550, 500))
        # screen.blit(player4, (500, 500))
        # screen.blit(player3, (450, 500))
        elif third > first and third > second and third > fourth:
            screen.blit(font.render(f"Winner is: Bråkiga Berit", True, gold), (100, 150))
            screen.blit(font.render("Oh Yeah!!", True, gold), (505, 425))
            screen.blit(player3_l, (510, 435))
        # screen.blit(player1, (550, 500))
        # screen.blit(player2, (500, 500))
        # screen.blit(player4, (450, 500))
        elif fourth > first and fourth > third and fourth > second:
            screen.blit(font.render(f"Winner is: Hänsynslöse Hannes", True, gold), (100, 150))
            screen.blit(font.render("Oh Yeah!!", True, gold), (505, 425))
            screen.blit(player4_l, (510, 435))
        # screen.blit(player1, (550, 500))
        # screen.blit(player2, (500, 500))
        # screen.blit(player3, (450, 500))
        elif first == second and first > third and first > fourth:
            screen.blit(font.render(f"It's a tie", True, gold), (100, 150))
            # screen.blit(player4, (550, 500))
            screen.blit(player1_l, (720, 435))
            screen.blit(player2_l, (690, 435))
        # screen.blit(player3, (450, 500))
        elif first == third and first > second and first > fourth:
            screen.blit(font.render(f"It's a tie", True, gold), (100, 150))
            # screen.blit(player4, (550, 500))
            screen.blit(player1_l, (720, 435))
            # screen.blit(player2, (450, 500))
            screen.blit(player3_l, (690, 435))
        elif first == fourth and first > third and first > second:
            screen.blit(font.render(f"It's a tie", True, gold), (100, 150))
            screen.blit(player4_l, (690, 435))
            screen.blit(player1_l, (720, 435))
        # screen.blit(player2, (450, 500))
        # screen.blit(player3, (550, 500))
        elif second == third and second > first and second > fourth:
            screen.blit(font.render(f"It's a tie", True, gold), (100, 150))
            # screen.blit(player4, (450, 500))
            # screen.blit(player1, (550, 500))
            screen.blit(player2_l, (690, 435))
            screen.blit(player3_l, (720, 435))
        elif second == fourth and second > third and second > first:
            screen.blit(font.render(f"It's a tie", True, gold), (100, 150))
            screen.blit(player4_l, (720, 435))
            # screen.blit(player1, (550, 500))
            screen.blit(player2_l, (690, 435))
        # screen.blit(player3, (450, 500))
        elif third == fourth and third > first and third > second:
            screen.blit(font.render(f"It's a tie", True, gold), (100, 150))
            screen.blit(player4_l, (720, 435))
            # screen.blit(player1, (550, 500))
            # screen.blit(player2, (450, 500))
            screen.blit(player3_l, (690, 435))
        elif third == fourth == second == first:
            screen.blit(font.render(f"It's a tie", True, gold), (100, 150))
            screen.blit(player4_l, (680, 435))
            screen.blit(player1_l, (700, 435))
            screen.blit(player2_l, (720, 435))
            screen.blit(player3_l, (740, 435))

        screen.blit(font2.render(f"Press [Q] to QUIT", True, white), (200, 90))
        screen.blit(font2.render(f"Press [P] to PLAY AGAIN", True, white), (200, 110))

        pygame.display.update()


def main_main_window():
    pygame.mixer.music.load("sound_and_music/music/rob_lounge.mp3")
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((800, 600))
    logo = pygame.image.load('images/gui/logga.png')
    play_sign = pygame.image.load('images/gui/play_game_logga.png')
    quit_sign = pygame.image.load('images/gui/Quitknapp.png')
    play_button = pygame.Rect(250, 250, 300, 100)
    quit_button = pygame.Rect(250, 350, 300, 100)
    pygame.draw.rect(screen, (0, 0, 0), play_button)
    pygame.draw.rect(screen, (0, 0, 0), quit_button)
    screen.blit(play_sign, (250, 250))
    screen.blit(quit_sign, (250, 350))
    screen.blit(logo, (50, 50))


if __name__ == '__main__':
    end_screen(4, 1, 10, 3)
