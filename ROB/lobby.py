import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
casino_bg = pygame.image.load('pics//casino.png')
statistics = pygame.image.load('pics//scoreboard.png')
make_bets = pygame.image.load('pics//make_your_bets.png')
fight_sign = pygame.image.load('pics//fight_sign.png')
screen.blit(casino_bg, (0, 0))
screen.blit(statistics, (100, 200))
screen.blit(make_bets, (350, 200))
screen.blit(fight_sign, (250, 50))
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.update()
