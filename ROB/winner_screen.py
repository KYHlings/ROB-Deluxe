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
dead = pygame.image.load("pics//player_dead.png")
winner_char = pygame.image.load("pics//winner.png")

def winner_screen(winner):
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
		screen.blit(dead, (400, 550))

		#for pix in range(550, 400):
		screen.blit(winner_char, (400, 500))
			#pygame.display.update()
		pygame.display.update()