import pygame
import sys
from ROB.fight import fight
from ROB.winner_screen import winner_screen
from ROB.end_screen import end_screen
# en lista över alla matcher
matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"], ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"], ["Boxare Bob", "Bråkiga Berit"]]
# lista på dom som bettar (listor i listan, beroende på match)
bet_list = [["Bråkiga Berit", "Hänsynslöse Hannes" ],["Slaktar Sune", "Boxare Bob"],["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"],["Boxare Bob", "Bråkiga Berit"],["Slaktar Sune", "Hänsynslöse Hannes"]]
# sätter font + storlek + bold
font = pygame.font.SysFont("Arial", 30, True)
# sätter storlek på skärmen
screen = pygame.display.set_mode((800, 600))
#laddar upp bilder för de olika betting-valörerna
ten = pygame.image.load("pics//10$.png")
minus_ten = pygame.image.load("pics//-10$.png")
fifty = pygame.image.load("pics//50$.png")
minus_fifty = pygame.image.load("pics//-50$.png")
# rektanglar för betting-valörerna
ten_button = pygame.Rect(430, 250, 71, 42)
minus_ten_button = pygame.Rect(505, 250, 71, 42)
fifty_button = pygame.Rect(430, 300, 71, 42)
minus_fifty_button = pygame.Rect(505, 300, 71, 42)
ten_button_2 = pygame.Rect(630, 250, 71, 42)
minus_ten_button_2 = pygame.Rect(705, 250, 71, 42)
fifty_button_2 = pygame.Rect(630, 300, 71, 42)
minus_fifty_button_2 = pygame.Rect(705, 300, 71, 42)
# laddar bilder på avatarer till karaktärerna
sune_head = pygame.image.load("pics//head_sune.png")
bob_head = pygame.image.load("pics//head_bob.png")
berit_head = pygame.image.load("pics//head_berit.png")
hannes_head = pygame.image.load("pics//head_hannes.png")
# skapar rektanglar för avatarer
head_sune_rect = pygame.Rect(390, 250, 40, 35)
head_bob_rect = pygame.Rect(390, 250, 40, 35)
head_berit_rect = pygame.Rect(390, 250, 40, 35)
head_hannes_rect = pygame.Rect(390, 250, 40, 35)
# målar ut avatarerna på skärmen
screen.blit(sune_head, (390, 250))
screen.blit(bob_head, (390, 300))
# målar ut texten till SCORE-rutan
def show_stats(score1, score2, score3, score4):
	screen.blit(font.render(f"SCORE: ", True, (255, 255, 255)), (50, 150))
	screen.blit(font.render(f"Slaktar Sune: {score1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Boxare Bob: {score2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Bråkiga Berit: {score3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Hänsynslöse Hannes: {score4}", True, (255, 255, 255)), (50, 350))
	screen.blit(font.render(f"MUSIC: ", True, (255, 255, 255)), (550, 10))
	minus, mute, plus = volume_buttons()


def lobby_window():
	# stoppar manin_menu musiken och laddar lobby-musiken
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music//casino_music.wav")
	pygame.mixer.music.play(-1)
	# laddar in lobby bakgrundsbilden och fight sign bilden
	casino_bg = pygame.image.load('pics//casino.png')
	fight_sign = pygame.image.load('pics//fight_sign.png')
	# Skapar en osynlig rektangel
	fight_button = pygame.Rect(250, 50, 300, 100)
	# Målar rektangeln svart på skärmen
	pygame.draw.rect(screen, (0, 0, 0), fight_button)
	# Målar upp bilderna casino och fight på skärmen
	screen.blit(casino_bg, (0, 0))
	screen.blit(fight_sign, (250, 50))
	# Returnar fight_button rektangeln
	return fight_button


def player_bars(winner):
	# Målar ut en text-sträng som visar den föregående vinnaren, med anitalias som True, färgen på texten vit och koordinater
	screen.blit(font.render(f"Previous winnner: {winner}", True, (255, 255, 255)), (100, 530))
	# Uppdaterar skärmen
	pygame.display.update()


def lobby():
	# anropar init i pygame som gör att vi kan använda alla pygame commands
	pygame.init()
	# anropar mixer init i pygame så att vi kan använda alla mixer commands
	pygame.mixer.init()
	# Sätter running till True
	running = True
	# Sätter score-variabeln till 100
	score = 100
	# Sätter en varibel volume till 0.5
	volume = 0.5
	# Sätter en variabel current_match till 0
	current_match = 0
	# Sätter en variabel better_1 till 0
	better_1 = 0
	# Sätter en variabel better_2 till 0
	better_2 = 0
	# Sätter en variabel better_1_0 till 0
	better_1_0 = 0
	# Sätter en variabel better_2_0 till 0
	better_2_0 = 0
	# Sätter en variabel för varje spelare med värdet 100 som vi får av variabeln score
	score_player1 = score
	score_player2 = score
	score_player3 = score
	score_player4 = score
	# Sätter att variabeln fight_button är en rektangel
	fight_button = lobby_window()
	#
	minus, mute, plus = volume_buttons()
	show_stats(score_player1, score_player2, score_player3, score_player4)
	screen.blit(sune_head, (390, 250))
	screen.blit(bob_head, (390, 300))
	while running:
		pygame.mixer.music.set_volume(volume)
		if current_match > 5:
			end_screen(score_player1, score_player2, score_player3, score_player4)
			return

		button_blittings(better_1, better_2, current_match)

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
						if bet_list[current_match][0] == "Bråkiga Berit":
							if better_1 >= score_player3:
								better_1 = score_player3
							else:
								better_1 += 10
						if bet_list[current_match][0] == "Slaktar Sune":
							if better_1 >= score_player1:
								better_1 = score_player1
							else:
								better_1 += 10
						if bet_list[current_match][0] == "Boxare Bob":
							if better_1 >= score_player2:
								better_1 = score_player2
							else:
								better_1 += 10

						print('hit')
						print(better_1)
					if ten_button_2.collidepoint(mx, my):
						if bet_list[current_match][1] == "Hänsynslöse Hannes":
							if better_2 >= score_player4:
								better_2 = score_player4
							else:
								better_2 += 10
						if bet_list[current_match][1] == "Boxare Bob":
							if better_2 >= score_player2:
								better_2 = score_player2
							else:
								better_2 += 10
						if bet_list[current_match][1] == "Bråkiga Berit":
							if better_2 >= score_player3:
								better_2 = score_player3
							else:
								better_2 += 10

						print('hit')
						print(better_2)
					if fifty_button.collidepoint(mx, my):
						if bet_list[current_match][0] == "Bråkiga Berit":
							if better_1 >= score_player3:
								better_1 = score_player3
							else:
								better_1 += 50
						if bet_list[current_match][0] == "Slaktar Sune":
							if better_1 >= score_player1:
								better_1 = score_player1
							else:
								better_1 += 50
						if bet_list[current_match][0] == "Boxare Bob":
							if better_1 >= score_player2:
								better_1 = score_player2
							else:
								better_1 += 50
						print('hit')
						print(better_1)
					if fifty_button_2.collidepoint(mx, my):
						if bet_list[current_match][1] == "Hänsynslöse Hannes":
							if better_2 >= score_player4:
								better_2 = score_player4
							else:
								better_2 += 50
						if bet_list[current_match][1] == "Boxare Bob":
							if better_2 >= score_player2:
								better_2 = score_player2
							else:
								better_2 += 50
						if bet_list[current_match][1] == "Bråkiga Berit":
							if better_2 >= score_player3:
								better_2 = score_player3
							else:
								better_2 += 50

						print('hit')
						print(better_2)
						#minus bet
					if minus_ten_button.collidepoint(mx, my):
						if bet_list[current_match][0] == "Bråkiga Berit":
							if better_1 <= 0:
								better_1 = 0
							else:
								better_1 -= 10
						if bet_list[current_match][0] == "Slaktar Sune":
							if better_1 <= 0:
								better_1 = 0
							else:
								better_1 -= 10
						if bet_list[current_match][0] == "Boxare Bob":
							if better_1 <= 0:
								better_1 = 0
							else:
								better_1 -= 10
						print('hit')
						print(better_1)
					if minus_ten_button_2.collidepoint(mx, my):
						if bet_list[current_match][1] == "Hänsynslöse Hannes":
							if better_2 <= 0:
								better_2 = 0
							else:
								better_2 -= 10
						if bet_list[current_match][1] == "Boxare Bob":
							if better_2 <= 0:
								better_2 = 0
							else:
								better_2 -= 10
						if bet_list[current_match][1] == "Bråkiga Berit":
							if better_2 <= 0:
								better_2 = 0
							else:
								better_2 -= 10

						print('hit')
						print(better_2)
					if minus_fifty_button.collidepoint(mx, my):
						if bet_list[current_match][0] == "Bråkiga Berit":
							if better_1 <= 0:
								better_1 = 0
							else:
								better_1 -= 50
						if bet_list[current_match][0] == "Slaktar Sune":
							if better_1 <= 0:
								better_1 = 0
							else:
								better_1 -= 50
						if bet_list[current_match][0] == "Boxare Bob":
							if better_1 <= 0:
								better_1 = 0
							else:
								better_1 -= 50
						print('hit')
						print(better_1)
					if minus_fifty_button_2.collidepoint(mx, my):
						if bet_list[current_match][1] == "Hänsynslöse Hannes":
							if better_2 <= 0:
								better_2 = 0
							else:
								better_2 -= 50
						if bet_list[current_match][1] == "Boxare Bob":
							if better_2 <= 0:
								better_2 = 0
							else:
								better_2 -= 50
						if bet_list[current_match][1] == "Bråkiga Berit":
							if better_2 <= 0:
								better_2 = 0
							else:
								better_2 -= 50
						print('hit')
						print(better_2)



					# Volume buttons
					if plus.collidepoint(mx, my):
						volume += 0.1
						print("höjer")
					if minus.collidepoint(mx, my):
						volume -= 0.1
						print("sänker")
					if mute.collidepoint(mx, my):
						volume = 0
						print("mute")

					# if head_sune_rect.collidepoint(mx, my):
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


def button_blittings(better_1, better_2, current_match):
	screen.blit(
		font.render(f"Next match:{matchup[current_match][0]} vs {matchup[current_match][1]} ", True, (255, 255, 255)),
		(50, 550))
	# betting ruta
	screen.blit(font.render("Betters:", True, (255, 255, 255)), (400, 150))
	screen.blit(font.render(f"{bet_list[current_match][0]} --- {bet_list[current_match][1]}", True, (255, 255, 255)),
				(400, 200))
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
	# total rects
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
	screen.blit(font.render(f"{better_1 * 2}", True, (255, 255, 255)), (445, 410))
	screen.blit(font.render(f"{better_2 * 2}", True, (255, 255, 255)), (645, 410))


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

