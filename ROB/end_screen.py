
from ROB.run import *
pygame.init()

font = pygame.font.SysFont("Arial", 40, True)
font2 = pygame.font.SysFont("Arial", 25)
black = (0, 0, 0)
gold = (207, 181, 59)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = [pygame.image.load('pics//end_screen_0.png')]
player1 = pygame.image.load('pics//walking_right_0.png')
player2 = pygame.image.load('pics//walking_right_green_0.png')
player3 = pygame.image.load('pics//walking_right_yellow_0.png')
player4 = pygame.image.load('pics//walking_right_purple_0.png')

player1_l = pygame.image.load('pics//walking_left_0.png')
player2_l = pygame.image.load('pics//walking_left_0_green.png')
player3_l = pygame.image.load('pics//walking_left_0_yellow.png')
player4_l = pygame.image.load('pics//walking_left_0_purple.png')

matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"], ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"], ["Boxare Bob", "Bråkiga Berit"]]
podium = pygame.image.load('pics//podium.png')

def end_screen(first, second, third, fourth):
	running = True
	while running:
		screen.blit(bg_image[0],(0, 0))
		screen.blit(podium, (700, 500))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_p:
					main()

		if first > second and third and fourth:
			screen.blit(font.render(f"Winner is: Slaktar Sune", True, (gold)), (screen_width/4, 50))
			screen.blit(player1_l, (710, 435))
			screen.blit(player4, (550, 500))
			screen.blit(player2, (500, 500))
			screen.blit(player3, (450, 500))
		if second > first and third and fourth:
			screen.blit(font.render(f"Winner is: Boxare Bob", True, (gold)), (screen_width / 4, 50))
			screen.blit(player2_l, (710, 435))
			screen.blit(player1, (550, 500))
			screen.blit(player4, (500, 500))
			screen.blit(player3, (450, 500))
		if third > first and second and fourth:
			screen.blit(font.render(f"Winner is: Bråkiga Berit", True, (gold)), (screen_width / 4, 50))
			screen.blit(player3_l, (710, 435))
			screen.blit(player1, (550, 500))
			screen.blit(player2, (500, 500))
			screen.blit(player4, (450, 500))
		if fourth > first and third and second:
			screen.blit(font.render(f"Winner is: Hänsynslöse Hannes", True, (gold)), (screen_width / 4, 50))
			screen.blit(player4_l, (710, 435))
			screen.blit(player1, (550, 500))
			screen.blit(player2, (500, 500))
			screen.blit(player3, (450, 500))



		screen.blit(font2.render(f"Press [Q] to QUIT", True, (black)), (200, 90))
		screen.blit(font2.render(f"Press [P] to PLAY AGAIN", True, (black)), (200, 110))

		pygame.display.update()

if __name__ == '__main__':
	end_screen(7, 4, 3, 1)
