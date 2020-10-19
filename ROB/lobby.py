import pygame
import sys
from ROB.fight import Fight, fight

pygame.init()


def lobby():
	fight_button = lobby_window()
	running = True
	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				#
				mx, my = pygame.mouse.get_pos()
				# kollar vilken knapp på musen som tryckts ned
				if event.button == 1:
					# kollar om musens position vid knapptryckningen kolliderar med playbutton
					if fight_button.collidepoint(mx, my):
						# stänger programmet
						fight_settings = Fight('1, 2')
						score = fight()
						fight_button = lobby_window()

			# uppdaterar displayen
			pygame.display.update()


def lobby_window():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music//casino_music.mp3")
	pygame.mixer.music.play(-1)
	screen = pygame.display.set_mode((800, 600))
	casino_bg = pygame.image.load('pics//casino.png')
	statistics = pygame.image.load('pics//scoreboard.png')
	make_bets = pygame.image.load('pics//make_your_bets.png')
	fight_sign = pygame.image.load('pics//fight_sign.png')
	fight_button = pygame.Rect(250, 50, 300, 100)
	pygame.draw.rect(screen, (0, 0, 0), fight_button)
	screen.blit(casino_bg, (0, 0))
	screen.blit(statistics, (100, 200))
	screen.blit(make_bets, (350, 200))
	screen.blit(fight_sign, (250, 50))
	return fight_button





