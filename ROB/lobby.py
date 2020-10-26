import pygame
import sys
from ROB.fight import fight
from ROB.winner_screen import winner_screen
from ROB.end_screen import end_screen

matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"], ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"], ["Boxare Bob", "Bråkiga Berit"]]
font = pygame.font.SysFont("Arial", 30, True)
screen = pygame.display.set_mode((800, 600))


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
	screen.blit(font.render(f"Winner is: {winner}", True, (255, 255, 255)), (150, 530))
	pygame.display.update()


def lobby():
	pygame.init()
	pygame.mixer.init()
	running = True
	score = 100
	volume = 0.5
	current_match = 0
	score_player1 = score
	score_player2 = score
	score_player3 = score
	score_player4 = score
	fight_button = lobby_window()
	minus, mute, plus = volume_buttons()
	show_stats(score_player1, score_player2, score_player3, score_player4)
	while running:
		pygame.mixer.music.set_volume(volume)
		screen.blit(font.render(f"Next match:{matchup[current_match][0]} vs {matchup[current_match][1]} ", True, (255, 255, 255)), (200, 500))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				# kollar position på musen
				mx, my = pygame.mouse.get_pos()
				# kollar vilken knapp på musen som tryckts ned
				if event.button == 1:
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
						if current_match == 6:
							end_screen(score_player1, score_player2, score_player3, score_player4)

						winner, loser = fight(current_match)
						print("Winner is player " + str(winner))
						current_match += 1
						winner_screen(winner, loser)
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
	if winner == "Slaktar Sune":
		score_player1 += 100
	if winner == "Boxare Bob":
		score_player2 += 100
	if winner == "Bråkiga Berit":
		score_player3 += 100
	if winner == "Hänsynslöse Hannes":
		score_player4 += 100
	screen.blit(font.render(f"SCORE: ", True, (255, 255, 255)), (50, 150))
	screen.blit(font.render(f"Slaktar Sune: {score_player1}", True, (255, 255, 255)), (50, 200))
	screen.blit(font.render(f"Boxare Bob: {score_player2}", True, (255, 255, 255)), (50, 250))
	screen.blit(font.render(f"Bråkiga Berit: {score_player3}", True, (255, 255, 255)), (50, 300))
	screen.blit(font.render(f"Hänsynslöse Hannes: {score_player4}", True, (255, 255, 255)), (50, 350))
	screen.blit(font.render(f"MUSIC: ", True, (255, 255, 255)), (550, 10))
	minus, mute, plus = volume_buttons()
	return score_player1, score_player2, score_player3, score_player4

