import pygame
import sys
from ROB.fight import fight, Player

matches = ["1,2", "3,4", "1,3", "2,4", "1,4", "2,3"]
screen = pygame.display.set_mode((800, 600))
score_player1 = 100
score_player2 = 100
score_player3 = 100
score_player4 = 100



def scoring(result, score_player1, score_player2, score_player3, score_player4):
	if result == 1:
		score_player1 += 100
	if result == 2:
		score_player2 += 100
	if result == 3:
		score_player3 += 100
	if result == 4:
		score_player4 += 100
	if result == 5:
		score_player1 += 0
	if result == 6:
		score_player2 += 0
	font = pygame.font.SysFont("Arial", 30, True)
	screen.blit(font.render(f"Player 1 score: {score_player1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Player 2 score: {score_player2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Player 3 score: {score_player3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Player 4 score: {score_player4}", True, (255, 255, 255)), (50, 350))


def lobby_window():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music//casino_music.wav")
	pygame.mixer.music.play(-1)
	casino_bg = pygame.image.load('pics//casino.png')
	make_bets = pygame.image.load('pics//make_your_bets.png')
	fight_sign = pygame.image.load('pics//fight_sign.png')
	fight_button = pygame.Rect(250, 50, 300, 100)
	pygame.draw.rect(screen, (0, 0, 0), fight_button)
	screen.blit(casino_bg, (0, 0))
	screen.blit(make_bets, (350, 200))
	screen.blit(fight_sign, (250, 50))
	return fight_button


def player_bars(score1, score2, winner):
	player1 = 0
	player2 = 0
	player3 = 0
	player4 = 0
	if winner == 1:
		player1 += winner
	if winner == 2:
		player2 += winner
	if winner == 3:
		player3 += winner
	if winner == 4:
		player4 += winner
	font = pygame.font.SysFont("Arial", 30, True)
	screen.blit(font.render(f"Winner is Player: {winner}", True, (255, 255, 255)), (150, 530))
	pygame.display.update()


def lobby():
	pygame.init()
	pygame.mixer.init()
	fight_button = lobby_window()
	running = True
	matchup = 0
	while running:
		scoring(0, score_player1, score_player2, score_player3, score_player4)
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
						print(f"P{winner}: {scoring(winner, score_player1, score_player2, score_player3, score_player4)}, P{loser}: 0")
						# måla upp lobbyn igen
						lobby_window()
						player_bars(scoring(winner, score_player1, score_player2, score_player3, score_player4), scoring(loser, score_player1, score_player2, score_player3, score_player4), winner)
						# gå vidare till nästa match
						matchup += matchup
		# uppdaterar displayen
		pygame.display.update()

