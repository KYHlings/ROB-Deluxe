import pygame
import sys
# TODO - Fixa så man kan se vem som vann bettet i winner-screen

pygame.init()
font = pygame.font.SysFont("Arial", 40, True)
font2 = pygame.font.SysFont("Arial", 15)
black = (0, 0, 0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = [pygame.image.load('images/arena_bakgrund_0.png'), pygame.image.load('images/arena_bakgrund_1.png')]
sune_dead = pygame.image.load("images/player_dead.png")
berit_dead = pygame.image.load("images/Berit_dead.png")
bob_dead = pygame.image.load("images/Bob_dead.png")
hannes_dead = pygame.image.load("images/Hannes_dead.png")
# sune_winner = pygame.image.load("images//winner.png")
# berit_winner = pygame.image.load("images//winner_berit.png")
# bob_winner = pygame.image.load("images//winner_bob.png")
# hannes_winner = pygame.image.load("images//winner_hannes.png")

def audience(current_match):
    hannes = pygame.image.load('images/walking_right_purple_0.png')
    berit = pygame.image.load('images/walking_right_yellow_0.png')
    sune = pygame.image.load('images/walking_right_0.png')
    bob = pygame.image.load('images/walking_right_green_0.png')
    if current_match == 0:
        screen.blit(hannes, (40, 170))
        screen.blit(berit, (70, 170))
    if current_match == 1:
        screen.blit(sune, (40, 170))
        screen.blit(bob, (70, 170))
    if current_match == 2:
        screen.blit(hannes, (40, 170))
        screen.blit(bob, (70, 170))
    if current_match == 3:
        screen.blit(sune, (40, 170))
        screen.blit(berit, (70, 170))
    if current_match == 4:
        screen.blit(bob, (40, 170))
        screen.blit(berit, (70, 170))
    if current_match == 5:
        screen.blit(sune, (40, 170))
        screen.blit(hannes, (70, 170))


def winner_screen(winner, loser, current_match):
    winner_char = pygame.image.load("images/winner.png")
    sune_winner = pygame.image.load("images/winner.png")
    berit_winner = pygame.image.load("images/winner_berit.png")
    bob_winner = pygame.image.load("images/winner_bob.png")
    hannes_winner = pygame.image.load("images/winner_hannes.png")
    running = True
    while running:
        screen.blit(bg_image[0],(0, 0))
        audience(current_match)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_SPACE:
                    if winner == "Slaktar Sune":
                        sune_winner = pygame.transform.flip(sune_winner, True, False)
                    if winner == "Boxare Bob":
                        bob_winner = pygame.transform.flip(bob_winner, True, False)
                    if winner == "Hänsynslöse Hannes":
                        hannes_winner = pygame.transform.flip(hannes_winner, True, False)
                    if winner == "Bråkiga Berit":
                        berit_winner = pygame.transform.flip(berit_winner, True, False)


        screen.blit(font.render(f"Winner is: {winner}", True, (255, 255, 255)), (screen_width/4, 50))
        screen.blit(font2.render(f"Press [SPACE] to celebrate", True, (255, 255, 255)), (screen_width/3, 90))
        screen.blit(font2.render("Press [ENTER] to continue", True, (255, 255, 255)), (screen_width/3, 105))
        winner_loser_cel(berit_winner, bob_winner, hannes_winner, loser, sune_winner, winner)
        #for pix in range(550, 400):

            #pygame.display.update()
        pygame.display.update()


def winner_loser_cel(berit_winner, bob_winner, hannes_winner, loser, sune_winner, winner):
    if loser == "Slaktar Sune":
        screen.blit(sune_dead, (400, 550))
    if loser == "Boxare Bob":
        screen.blit(bob_dead, (400, 550))
    if loser == "Hänsynslöse Hannes":
        screen.blit(hannes_dead, (400, 550))
    if loser == "Bråkiga Berit":
        screen.blit(berit_dead, (400, 550))
    if winner == "Slaktar Sune":
        screen.blit(sune_winner, (400, 500))
    if winner == "Boxare Bob":
        screen.blit(bob_winner, (400, 500))
    if winner == "Hänsynslöse Hannes":
        screen.blit(hannes_winner, (400, 500))
    if winner == "Bråkiga Berit":
        screen.blit(berit_winner, (400, 500))
