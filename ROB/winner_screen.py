import pygame
import sys

font = pygame.font.SysFont("Arial", 40, True)
font2 = pygame.font.SysFont("Arial", 15)
black = (0, 0, 0)
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = [pygame.image.load('pics//arena_bakgrund_0.png'), pygame.image.load('pics//arena_bakgrund_1.png')]
sune_dead= pygame.image.load("pics//player_dead.png")
berit_dead = pygame.image.load("pics//Berit_dead.png")
bob_dead = pygame.image.load("pics//Bob_dead.png")
hannes_dead = pygame.image.load("pics//Hannes_dead.png")
winner_char = pygame.image.load("pics//winner.png")

def winner_screen(winner, loser):
	winner_char = pygame.image.load("pics//winner.png")
	running = True
	while running:
		screen.blit(bg_image[0],(0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					return
				if event.key == pygame.K_SPACE:
					winner_char = pygame.transform.flip(winner_char, True, False)

		screen.blit(font.render(f"Winner is: {winner}", True, (255, 255, 255)), (screen_width/4, 50))
		screen.blit(font2.render(f"Press [SPACE] to celebrate", True, (255, 255, 255)), (screen_width/3, 90))
		if loser == "Slaktar Sune":
			screen.blit(sune_dead, (400, 550))
		if loser == "Boxare Bob":
			screen.blit(bob_dead, (400, 550))
		if loser == "Hänsynslöse Hannes":
			screen.blit(hannes_dead, (400, 550))
		if loser == "Bråkiga Berit":
			screen.blit(berit_dead, (400, 550))
		#for pix in range(550, 400):
		screen.blit(winner_char, (400, 500))
			#pygame.display.update()
		pygame.display.update()