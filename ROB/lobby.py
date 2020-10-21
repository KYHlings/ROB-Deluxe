import pygame
import sys
from ROB.fight import fight

matches = ["1,2", "3,4", "1,3", "2,4", "1,4", "2,3"]
font = pygame.font.SysFont("Arial", 30, True)
screen = pygame.display.set_mode((800, 600))


def show_stats(score1, score2, score3, score4):
	screen.blit(font.render(f"Player 1 score: {score1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Player 2 score: {score2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Player 3 score: {score3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Player 4 score: {score4}", True, (255, 255, 255)), (50, 350))
	screen.blit(font.render(f"VOLUME: ", True, (255, 255, 255)), (550, 10))
	screen.blit(font.render(f"Vol+ : [ U ]", True, (255, 255, 255)), (680, 10))
	screen.blit(font.render(f"Vol- : [ J ]", True, (255, 255, 255)), (680, 40))


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


def player_bars(winner):
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
	screen.blit(font.render(f"Winner is Player: {winner}", True, (255, 255, 255)), (150, 530))
	pygame.display.update()


def lobby():
	pygame.init()
	pygame.mixer.init()
	running = True
	matchup = 0
	score = 100
	score_player1 = score
	score_player2 = score
	score_player3 = score
	score_player4 = score
	fight_button = lobby_window()
	while running:
		show_stats(score_player1, score_player2, score_player3, score_player4)
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
						winner = fight()
						print("Winner is player " + str(winner))

										# printar score
						if winner == 1:
							print(show_score(score_player1, score_player2, score_player3, score_player4, winner))
						else:
							print(show_score(score_player1, score_player2, score_player3, score_player4, winner))
										# måla upp lobbyn igen
						lobby_window()
						player_bars(winner)
						score_player1, score_player2, score_player3, score_player4 = show_score(score_player1, score_player2, score_player3, score_player4, winner)
					# show_stats(scoring_p1(winner, score_player1), scoring_p2(winner, score_player2), scoring_p3(winner, score_player3), scoring_p4(winner, score_player4))

		# uppdaterar displayen
		pygame.display.update()


def show_score(score_player1, score_player2, score_player3, score_player4, winner):
	if winner == 1:
		score_player1 += 100
	if winner == 2:
		score_player2 += 100
	if winner == 3:
		score_player3 += 100
	if winner == 4:
		score_player4 += 100
	screen.blit(font.render(f"Player 1 score: {score_player1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Player 2 score: {score_player2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Player 3 score: {score_player3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Player 4 score: {score_player4}", True, (255, 255, 255)), (50, 350))
	return score_player1, score_player2, score_player3, score_player4

