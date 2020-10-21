import pygame
import sys

font = pygame.font.SysFont("Arial", 40, True)
black = (0, 0, 0)
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = [pygame.image.load('pics//arena_bakgrund_0.png'), pygame.image.load('pics//arena_bakgrund_1.png')]


def winner_screen(winner):
	running = True
	while running:
		screen.blit(bg_image[0],(0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					return


		screen.blit(font.render(f"Winner is: {winner}", True, (255, 255, 255)), (50, 50))
		pygame.display.update()