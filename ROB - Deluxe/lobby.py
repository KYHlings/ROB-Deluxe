import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
casino_bg = pygame.image.load('pics//casino.png')
screen.blit(casino_bg, (0, 0))
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.update()