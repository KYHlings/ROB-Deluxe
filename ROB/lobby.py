import pygame
import sys
from ROB.fight import fight, Player

matches = ["1,2", "3,4", "1,3", "2,4", "1,4", "2,3"]


def lobby():
	pygame.init()
	pygame.mixer.init()
	fight_button = lobby_window()
	running = True
	matchup = 0

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
			# kollar position på musen
				mx, my = pygame.mouse.get_pos()
			# kollar vilken knapp på musen som tryckts ned
				if event.button == 1:
			# kollar om musens position vid knapptryckningen kolliderar med playbutton
					if fight_button.collidepoint(mx, my):
			# starta en fight och få resultatet tillbaka
						winner, loser = fight()
						print("Winner is player " + str(winner))

			# printar score
						print(f"P{winner}: {scoring(winner)}, P{loser}: 0")
			# måla upp lobbyn igen
						lobby_window()
			# gå vidare till nästa match
						matchup += matchup
		# uppdaterar displayen
		pygame.display.update()


def scoring(result):
	score_player1 = 0
	score_player2 = 0
	score_player3 = 0
	score_player4 = 0
	if result == 1:
		score_player1 += 100
		return score_player1
	if result == 2:
		score_player2 += 100
		return score_player2
	if result == 3:
		score_player3 += 100
		return score_player3
	if result == 4:
		score_player4 += 100
		return score_player4


def lobby_window():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music//casino_music.wav")
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
