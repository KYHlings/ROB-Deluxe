import pygame
import sys
from ROB.fight import fight
from ROB.winner_screen import winner_screen
from ROB.end_screen import end_screen

matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"], ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"], ["Boxare Bob", "Bråkiga Berit"]]
bet_list = [["Bråkiga Berit", "Hänsynslöse Hannes" ],["Slaktar Sune", "Boxare Bob"],["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"],["Boxare Bob", "Bråkiga Berit"],["Slaktar Sune", "Hänsynslöse Hannes"]]
font = pygame.font.SysFont("Arial", 30, True)
screen = pygame.display.set_mode((800, 600))

ten = pygame.image.load("pics//10$.png")
minus_ten = pygame.image.load("pics//-10$.png")
fifty = pygame.image.load("pics//50$.png")
minus_fifty = pygame.image.load("pics//-50$.png")
ten_button = pygame.Rect(430, 250, 71, 42)
minus_ten_button = pygame.Rect(505, 250, 71, 42)
fifty_button = pygame.Rect(430, 300, 71, 42)
minus_fifty_button = pygame.Rect(505, 300, 71, 42)
ten_button_2 = pygame.Rect(630, 250, 71, 42)
minus_ten_button_2 = pygame.Rect(705, 250, 71, 42)
fifty_button_2 = pygame.Rect(630, 300, 71, 42)
minus_fifty_button_2 = pygame.Rect(705, 300, 71, 42)



# ten_button_2 = pygame.image.load("pics//10$.png")
# minus_ten_button_2 = pygame.image.load("pics//-10$.png")
# fifty_button_2 = pygame.image.load("pics//50$.png")
# minus_fifty_button_2 = pygame.image.load("pics//-50$.png")



def show_stats(score1, score2, score3, score4):
	screen.blit(font.render(f"SCORE: ", True, (255, 255, 255)), (50, 150))
	screen.blit(font.render(f"Slaktar Sune: {score1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Boxare Bob: {score2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Bråkiga Berit: {score3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Hänsynslöse Hannes: {score4}", True, (255, 255, 255)), (50, 350))
	screen.blit(font.render(f"MUSIC: ", True, (255, 255, 255)), (550, 10))
	minus, mute, plus = volume_buttons()


def lobby_window():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music//casino_music.wav")
	pygame.mixer.music.play(-1)
	casino_bg = pygame.image.load('pics//casino.png')
	# make_bets = pygame.image.load('pics//make_your_bets.png')
	fight_sign = pygame.image.load('pics//fight_sign.png')
	fight_button = pygame.Rect(250, 50, 300, 100)
	pygame.draw.rect(screen, (0, 0, 0), fight_button)
	screen.blit(casino_bg, (0, 0))
	# screen.blit(make_bets, (350, 200))
	screen.blit(fight_sign, (250, 50))
	return fight_button


def player_bars(winner):
	screen.blit(font.render(f"Previous winnner: {winner}", True, (255, 255, 255)), (100, 530))
	pygame.display.update()


def lobby():
	pygame.init()
	pygame.mixer.init()
	running = True
	score = 100
	volume = 0.5
	current_match = 0
	better_1 = 0
	better_2 = 0
	score_player1 = score
	score_player2 = score
	score_player3 = score
	score_player4 = score
	fight_button = lobby_window()
	minus, mute, plus = volume_buttons()
	show_stats(score_player1, score_player2, score_player3, score_player4)

	while running:
		pygame.mixer.music.set_volume(volume)
		if current_match > 5:
			end_screen(score_player1, score_player2, score_player3, score_player4)
			return

		screen.blit(font.render(f"Next match:{matchup[current_match][0]} vs {matchup[current_match][1]} ", True, (255, 255, 255)), (50, 550))
		# betting ruta
		screen.blit(font.render("Betters:", True, (255, 255, 255)), (400, 150))
		screen.blit(font.render(f"{bet_list[current_match][0]} --- {bet_list[current_match][1]}", True, (255, 255, 255)), (400, 200))
		# bets 1
		pygame.draw.rect(screen, (0, 0, 0), ten_button)
		pygame.draw.rect(screen, (0, 0, 0), minus_ten_button)
		pygame.draw.rect(screen, (0, 0, 0), fifty_button)
		pygame.draw.rect(screen, (0, 0, 0), minus_fifty_button)
		screen.blit(ten, (430, 250))
		screen.blit(minus_ten, (505, 250))
		screen.blit(fifty, (430, 300))
		screen.blit(minus_fifty, (505, 300))
		# bets 2
		pygame.draw.rect(screen, (0, 0, 0), ten_button_2)
		pygame.draw.rect(screen, (0, 0, 0), minus_ten_button_2)
		pygame.draw.rect(screen, (0, 0, 0), fifty_button_2)
		pygame.draw.rect(screen, (0, 0, 0), minus_fifty_button_2)
		screen.blit(ten, (630, 250))
		screen.blit(minus_ten, (705, 250))
		screen.blit(fifty, (630, 300))
		screen.blit(minus_fifty, (705, 300))
		#total rects
		total1 = pygame.Rect(430, 350, 146, 50)
		pygame.draw.rect(screen, (0, 0, 0), total1)
		total2 = pygame.Rect(630, 350, 146, 50)
		pygame.draw.rect(screen, (0, 0, 0), total2)
		screen.blit(font.render(f"{better_1}", True, (255, 255, 255)), (445, 360))
		screen.blit(font.render(f"{better_2}", True, (255, 255, 255)), (645, 360))
		# confirm rects
		black_bg_rect = pygame.Rect(430, 405, 146, 50)
		pygame.draw.rect(screen, (0, 0, 0), black_bg_rect)
		black_bg_rect2 = pygame.Rect(630, 405, 146, 50)
		pygame.draw.rect(screen, (0, 0, 0), black_bg_rect2)
		screen.blit(font.render(f"{better_1*2}", True, (255, 255, 255)), (445, 410))
		screen.blit(font.render(f"{better_2*2}", True, (255, 255, 255)), (645, 410))



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				# kollar position på musen
				mx, my = pygame.mouse.get_pos()
				# kollar vilken knapp på musen som tryckts ned
				if event.button == 1:
					# plus bet
					if ten_button.collidepoint(mx, my):
						better_1 += 10


						print('hit')
						print(better_1)
					if ten_button_2.collidepoint(mx, my):
						better_2 += 10
						print('hit')
						print(better_2)
					if fifty_button.collidepoint(mx, my):
						better_1 += 50
						print('hit')
						print(better_1)
					if fifty_button_2.collidepoint(mx, my):
						better_2 += 50
						print('hit')
						print(better_2)
						#minus bet
					if minus_ten_button.collidepoint(mx, my):
						better_1 -= 10
						print('hit')
						print(better_1)
					if minus_ten_button_2.collidepoint(mx, my):
						better_2 -= 10
						print('hit')
						print(better_2)
					if minus_fifty_button.collidepoint(mx, my):
						better_1 -= 50
						print('hit')
						print(better_1)
					if minus_fifty_button_2.collidepoint(mx, my):
						better_2 -= 50
						print('hit')
						print(better_2)

						#total buttons



					if plus.collidepoint(mx, my):
						volume += 0.1
						print("höjer")
					if minus.collidepoint(mx, my):
						volume -= 0.1
						print("sänker")
					if mute.collidepoint(mx, my):
						volume = 0
						print("mute")



					# kollar om musens position vid knapptryckningen kolliderar med playbutton
					if fight_button.collidepoint(mx, my):
						# starta en fight och få resultatet tillbaka
						#if current_match > 5:
							#end_screen(score_player1, score_player2, score_player3, score_player4)

						winner, loser = fight(current_match)
						print("Winner is player " + str(winner))
						winner_screen(winner, loser, current_match)
						current_match += 1
						# printar score
						if winner == 1:
							print(show_score(score_player1, score_player2, score_player3, score_player4, winner))
						else:
							print(show_score(score_player1, score_player2, score_player3, score_player4, winner))
						# måla upp lobbyn igen
						lobby_window()

							#player_bars(winner)
						score_player1, score_player2, score_player3, score_player4 = show_score(score_player1, score_player2, score_player3, score_player4, winner)
					# show_stats(scoring_p1(winner, score_player1), scoring_p2(winner, score_player2), scoring_p3(winner, score_player3), scoring_p4(winner, score_player4))


		# uppdaterar displayen
		pygame.display.update()


def volume_buttons():
	plus = screen.blit(font.render(f"+", True, (255, 255, 255)), (700, 10))
	minus = screen.blit(font.render(f"-", True, (255, 255, 255)), (730, 9))
	mute = screen.blit(font.render(f"Mute", True, (255, 255, 255)), (710, 40))
	return minus, mute, plus


def show_score(score_player1, score_player2, score_player3, score_player4, winner):
	score_player1, score_player2, score_player3, score_player4 = winner_points(score_player1, score_player2,
																			   score_player3, score_player4, winner)
	screen.blit(font.render(f"SCORE: ", True, (255, 255, 255)), (50, 150))
	screen.blit(font.render(f"Slaktar Sune: {score_player1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Boxare Bob: {score_player2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Bråkiga Berit: {score_player3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Hänsynslöse Hannes: {score_player4}", True, (255, 255, 255)), (50, 350))
	screen.blit(font.render(f"MUSIC: ", True, (255, 255, 255)), (550, 10))
	minus, mute, plus = volume_buttons()
	return score_player1, score_player2, score_player3, score_player4



def winner_points(score_player1, score_player2, score_player3, score_player4, winner):
	if winner == "Slaktar Sune":
		score_player1 += 100
	if winner == "Boxare Bob":
		score_player2 += 100
	if winner == "Bråkiga Berit":
		score_player3 += 100
	if winner == "Hänsynslöse Hannes":
		score_player4 += 100
	return score_player1, score_player2, score_player3, score_player4

