def won_bet_calc(bet_counter, better_1, better_2, made_bet_1, made_bet_2, score_player1, score_player2, score_player3,
				 score_player4, winner):
	# bettare berit vs hannes
	if bet_counter == 1:
		# berit
		if made_bet_1 == winner:
			score_player3 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player3 -= better_1
		# bob
		if made_bet_2 == winner:
			score_player4 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player4 -= better_2
	# bettare sune vs bob
	if bet_counter == 2:
		# sune
		if made_bet_1 == winner:
			score_player1 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player1 -= better_1
		# bob
		if made_bet_2 == winner:
			score_player2 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player2 -= better_2
	# bettare bob vs hannes
	if bet_counter == 3:
		# bob
		if made_bet_1 == winner:
			score_player2 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player2 -= better_1
		# hannes
		if made_bet_2 == winner:
			score_player4 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player4 -= better_2
	# bettare sune vs berit
	if bet_counter == 4:
		# sune
		if made_bet_1 == winner:
			score_player1 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player1 -= better_1
		# berit
		if made_bet_2 == winner:
			score_player3 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player3 -= better_2
	# bettare bob vs berit
	if bet_counter == 5:
		# bob
		if made_bet_1 == winner:
			score_player2 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player2 -= better_1
		# berit
		if made_bet_2 == winner:
			score_player3 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player3 -= better_2
	# bettare sune vs hannes
	if bet_counter == 6:
		# sune
		if made_bet_1 == winner:
			score_player1 += (better_1 * 2)
		if made_bet_1 != winner:
			score_player1 -= better_1
		# hannes
		if made_bet_2 == winner:
			score_player4 += (better_2 * 2)
		if made_bet_2 != winner:
			score_player4 -= better_2
	return score_player1, score_player2, score_player3, score_player4


def bet_head_pfp(berit_pos, bob_pos, current_match, hannes_pos, sune_pos):
	if current_match == 0:
		sune_pos = 250
		bob_pos = 300
		# 1
		screen.blit(sune_head, (390, 250))
		screen.blit(bob_head, (390, 300))
		# 2
		screen.blit(sune_head, (590, 250))
		screen.blit(bob_head, (590, 300))
	if current_match == 1:
		berit_pos = 250
		hannes_pos = 300
		# 1
		screen.blit(berit_head, (390, 250))
		screen.blit(hannes_head, (390, 300))
		# 2
		screen.blit(berit_head, (590, 250))
		screen.blit(hannes_head, (590, 300))
	if current_match == 2:
		sune_pos = 250
		berit_pos = 300
		# 1
		screen.blit(sune_head, (390, 250))
		screen.blit(berit_head, (390, 300))
		# 2
		screen.blit(sune_head, (590, 250))
		screen.blit(berit_head, (590, 300))
	if current_match == 3:
		bob_pos = 250
		hannes_pos = 300
		# 1
		screen.blit(bob_head, (390, 250))
		screen.blit(hannes_head, (390, 300))
		# 2
		screen.blit(bob_head, (590, 250))
		screen.blit(hannes_head, (590, 300))
	if current_match == 4:
		sune_pos = 250
		hannes_pos = 300
		# 1
		screen.blit(sune_head, (390, 250))
		screen.blit(hannes_head, (390, 300))
		# 2
		screen.blit(sune_head, (590, 250))
		screen.blit(hannes_head, (590, 300))
		bob_pos = 250
		berit_pos = 300
		# 1
		screen.blit(bob_head, (390, 250))
		screen.blit(berit_head, (390, 300))
		# 2
		screen.blit(bob_head, (590, 250))
		screen.blit(berit_head, (590, 300))
	if current_match == 5:
		bob_pos = 250
		berit_pos = 300
		# 1
		screen.blit(bob_head, (390, 250))
		screen.blit(berit_head, (390, 300))
		# 2
		screen.blit(bob_head, (590, 250))
		screen.blit(berit_head, (590, 300))
	return berit_pos, bob_pos, hannes_pos, sune_pos


def bet_p2(better_2, current_match, head_berit_rect_1, head_bob_rect_1, head_hannes_rect_1, head_sune_rect_1,
		   made_bet_2, mx, my, score_player2, score_player3, score_player4):
	# player 2 bet
	if ten_button_2.collidepoint(mx, my):
		if bet_list[current_match][0] == "Bråkiga Berit":
			if better_2 >= score_player3:
				better_2 = score_player3
			else:
				better_2 += 10
		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			if better_2 >= score_player4:
				better_2 = score_player4
			else:
				better_2 += 10
		if bet_list[current_match][0] == "Boxare Bob":
			if better_2 >= score_player2:
				better_2 = score_player2
			else:
				better_2 += 10
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
	# bestämmer vilken fighter som spelare 2 väljer att betta på
	# om spelaren bettar på sune
	if head_sune_rect_1.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_2 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_2)

	# om spelaren bettar på Bob
	if head_bob_rect_1.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_2 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_2)

	# om spelaren bettar på Berit
	if head_berit_rect_1.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_2 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_2)

	# om spelaren bettar på Hannes
	if head_hannes_rect_1.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_2 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_2)

	return better_2, made_bet_2


def bet_p1(better_1, current_match, head_berit_rect, head_bob_rect, head_hannes_rect, head_sune_rect, made_bet_1, mx,
		   my, score_player1, score_player2, score_player3):
	# player 1 bet
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

		print('hit')
		print(better_1)
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
	# bestämmer vilken fighter som spelare 1 väljer att betta på
	# om spelaren bettar på Sune
	if head_sune_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Slaktar Sune"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("sune selected")
			print(made_bet_1)

	# om spelaren bettar på Bob
	if head_bob_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Boxare Bob"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("bob selected")
			print(made_bet_1)

	# om spelaren bettar på Berit
	if head_berit_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Bråkiga Berit"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("berit selected")
			print(made_bet_1)

	# om spelaren bettar på Hannes
	if head_hannes_rect.collidepoint(mx, my):
		if bet_list[current_match][0] == "Slaktar Sune":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Boxare Bob":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Bråkiga Berit":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

		if bet_list[current_match][0] == "Hänsynslöse Hannes":
			made_bet_1 = "Hänsynslöse Hannes"
			pygame.draw.rect(screen, (0, 0, 0), fight_button)
			screen.blit(fight_sign, (250, 50))
			print("hannes selected")
			print(made_bet_1)

	return better_1, made_bet_1


def show_bet_buttons(better_1, better_2, current_match):
	screen.blit(
		font.render(f"Next match:{matchup[current_match][0]} vs {matchup[current_match][1]} ", True, (255, 255, 255)),
		(50, 550))
	# betting ruta
	screen.blit(font.render("Betters:", True, (255, 255, 255)), (430, 150))
	screen.blit(font.render(f"{bet_names_list[current_match][0]}", True, (255, 255, 255)),
				(430, 200))
	screen.blit(font.render(f"{bet_names_list[current_match][1]}", True, (255, 255, 255)),
				(630, 200))
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
