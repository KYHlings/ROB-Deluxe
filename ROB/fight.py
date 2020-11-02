import sys
import pygame
import os
import time

# grundinställningar
# centrerar bildrutan
os.environ["SDL_VIDEO_CENTERED"] = "1"
# sätter färgen svart i variabeln black
black = (0, 0, 0)
# den startar pygame så man får tillgång till commandsen
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# laddar in bilder på bakgrund och gubbarna
bg_image = [pygame.image.load('pics//arena_bakgrund_0.png'), pygame.image.load('pics//arena_bakgrund_1.png')]
hannes = pygame.image.load('pics//walking_right_purple_0.png')
berit = pygame.image.load('pics//walking_right_yellow_0.png')
sune = pygame.image.load('pics//walking_right_0.png')
bob = pygame.image.load('pics//walking_right_green_0.png')
matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"],
           ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"],
           ["Boxare Bob", "Bråkiga Berit"]]

# tar current_match som indata i funktionen audience
def audience(current_match):
    # bestämmer vem som ska stå i publiken beroende på vilken siffra current_match blir
    if current_match == 0:
        screen.blit(hannes, (40, 170))
        screen.blit(berit, (70, 170))
    if current_match == 1:
        screen.blit(sune, (40, 170))
        screen.blit(bob, (70, 170))
    if current_match == 2:
        screen.blit(hannes, (40, 170))
        screen.blit(bob, (70, 170))
    if current_match == 3:
        screen.blit(sune, (40, 170))
        screen.blit(berit, (70, 170))
    if current_match == 4:
        screen.blit(bob, (40, 170))
        screen.blit(berit, (70, 170))
    if current_match == 5:
        screen.blit(sune, (40, 170))
        screen.blit(hannes, (70, 170))



# ljudeffekter
effect_punch = pygame.mixer.Sound('music//PUNCH.wav')
effect_dead = pygame.mixer.Sound('music//Wilhelm_Scream.ogg')
effect_KICK = pygame.mixer.Sound('music//KICK.wav')

# fps
fps_clock = pygame.time.Clock()
fps = 120

# TODO loopa bakrundsbilderna
screen.blit(bg_image[0], (0, 0))
screen.blit(bg_image[1], (0, 0))
font = pygame.font.SysFont("Arial", 15)

#gör en funktion för musiken i fightrutan
def fight_music():
    #stoppar föregående låt
    pygame.mixer.music.stop()
    # laddar in fight-låten
    pygame.mixer.music.load('music//fight_music.ogg')
    # spelar fightlåten om och om igen
    pygame.mixer.music.play(-1)


# gör en klass som heter player så tar vi pygame.sprite.Sprite som indata som bestämmer att objektet är en sprite
class Player(pygame.sprite.Sprite):
     # sätter grundinställningar för varje Player som skapas
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # bestämmer all hastighet för gubbarnas rörelser i pixlar
        self.vel = 5
        # bestämmer vilken bild som ska visas i images listan över spelarens olika bilder
        self.frame = 0
        # bestämmer vänster och höger riktning
        self.left = False
        self.right = False
        # skapar en variabel för spelarens storlek som ändras senare
        self.rect = (0, 0, 0, 0)
        # skapar en tom lista där vi senare ska lagra dom bilder karaktärerna ska ha
        self.images = []
        # skapar vi en variabel för karaktärernas health power
        self.hp = 100
        # skapar en variabel som bestämmer om spelaren lever eller inte
        self.dead = False

# skapar en funktion med self och match som indata som gör att rätt bild laddas in till rätt match
def player2_pics(self, match):
    # Sune är röd, Bob är grön, Berit är gul, Hannes är lila
    # Sune vs Bob
    if match == 0:
        print("hej match 1")
        print(len(player1.images))
        print(player1.frame)
        # skapar en loop som går mellan siffrorna 1-3
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Berit vs Hannes
    if match == 1:
        print("hej match 2")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_yellow_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Sune vs Berit
    if match == 2:
        print("hej match 3")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Bob vs Hannes
    if match == 3:
        print("hej match 4")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_green_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Sune vs Hannes
    if match == 4:
        print("hej match 5")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Bob vs Berit
    if match == 5:
        print("hej match 6")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_green_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)


def player1_pics(self, match):
    # Sune är röd, Bob är grön, Berit är gul, Hannes är lila
    # Sune vs Bob

    # TODO kan möjligvis krasha på index error för att player1.frame är 2, håll koll vid testning.
    if match == 0:
        print("hej match 1")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_green_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Berit vs Hannes

    if match == 1:
        print("hej match 2")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_purple_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Sune vs Berit

    if match == 2:
        print("hej match 3")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_yellow_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Bob vs Hannes

    if match == 3:
        print("hej match 4")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_purple_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Sune vs Hannes

    if match == 4:
        print("hej match 5")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_purple_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)

    # Bob vs Berit
    if match == 5:
        print("hej match 6")
        print(len(player1.images))
        print(player1.frame)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('pics', 'walking_right_yellow_' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(black)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)


player1 = Player()
# player1_pics(player1)
# player1.rect.x = 720
# player1.rect.y = 200
player1.hp = 100
player2 = Player()
# player2_pics(player2)
# player2.rect.x = 60
# player2.rect.y = 200
player2.hp = 100

# spawnar spelare


# lägger alla spelare i en sprite grupp
player_list = pygame.sprite.Group()
player_list.add(player1, player2)


def player_bars(which, current_match):
    font = pygame.font.SysFont("Arial", 20)
    if which == 1:
        screen.blit(font.render(f"{matchup[current_match][0]}", True, (255, 255, 255)), (50, 20))
    if which == 2:
        screen.blit(font.render(f"{matchup[current_match][1]}", True, (255, 255, 255)), (550, 20))


def healthbar(player1, player2):
    if player1.hp > -10:
        bg_bar1 = pygame.Rect(550, 50, 200, 50)
        hp_bar1 = pygame.Rect(550, 50, 200 * (player1.hp * 0.01), 50)
        pygame.draw.rect(screen, (255, 0, 0), bg_bar1)
        pygame.draw.rect(screen, (0, 255, 0), hp_bar1)
    if player2.hp > -10:
        bg_bar2 = pygame.Rect(50, 50, 200, 50)
        hp_bar2 = pygame.Rect(50, 50, 200 * (player2.hp * 0.01), 50)
        pygame.draw.rect(screen, (255, 0, 0), bg_bar2)
        pygame.draw.rect(screen, (0, 255, 0), hp_bar2)
    pygame.display.update()


def collision(player1, player2):
    # kollar om kollision har skett
    col = pygame.sprite.collide_rect(player1, player2)
    if col == True:
        return True


def player_movement(player1, player2):
    # Grund inställningar för position
    player1.rect.y += player1.vel
    player2.rect.y += player2.vel
    if player1.rect.y == 500:
        player1.vel = 0
    if player2.rect.y == 500:
        player2.vel = 0
    keys = pygame.key.get_pressed()

    # TODO det finns en bug där man flyger utanför skärmen om spelarna kolliderar och går åt ett håll tillsammans
    # FIGHTER 1
    # vänster
    if keys[pygame.K_LEFT] and player1.rect.x > player1.vel:
        player1.left = True
        player1.right = False
        if collision(player1, player2) == True:
            if player1.left == True:
                player1.rect.x += 5
        player1.rect.x -= 1
        player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)
        player1.frame += 1
        if player1.frame == 2:
            player1.frame = 0

    # höger
    if keys[pygame.K_RIGHT] and player1.rect.x < screen_width - 40:
        player1.left = False
        player1.right = True
        if collision(player1, player2) == True:
            if player1.right == True:
                player1.rect.x -= 5
        player1.rect.x += 1
        player1.frame += 1
        if player1.frame == 2:
            player1.frame = 0
        player1.image = player1.images[player1.frame]

    # HOPP
    if keys[pygame.K_RCTRL]:
        # hoppets höjd
        player1.rect.y -= 15
        # dragningskraft
        player1.vel = 3
        # invisible border max hopphöjd
        if player1.rect.y < 200:
            player1.vel = 20
    # lägsta punkt
    if player1.rect.y > 500:
        player1.rect.y = 500

    # FIGTER 2
    # vänster
    if keys[pygame.K_a] and player2.rect.x > player2.vel:
        player2.left = True
        player2.right = False
        if collision(player1, player2) == True:
            if player2.left == True:
                player2.rect.x += 5
        player2.rect.x -= 1
        player2.image = pygame.transform.flip(player2.images[player2.frame], True, False)
        player2.frame += 1
        if player2.frame == 2:
            player2.frame = 0

    # höger
    if keys[pygame.K_d] and player2.rect.x < screen_width - 40:
        player2.left = False
        player2.right = True
        if collision(player1, player2) == True:
            if player2.right == True:
                player2.rect.x -= 5
        player2.rect.x += 1
        player2.frame += 1
        if player2.frame == 2:
            player2.frame = 0
        player2.image = player2.images[player2.frame]

    # HOPP
    if keys[pygame.K_SPACE]:
        # hoppets höjd
        player2.rect.y -= 15
        # dragningskraft
        player2.vel = 3
        # invisible border max hopphöjd
        if player2.rect.y < 200:
            player2.vel = 20
    # lägsta punkt
    if player2.rect.y > 500:
        player2.rect.y = 500


def punch_and_kick(current_match):
    # kollar om en knapp är nedtryckt
    if keys.type == pygame.KEYDOWN:
        # fighter1 slag och spark
        if keys.key == pygame.K_UP:
            if collision(player1, player2) == True:
                # hit = pygame.time.get_ticks()
                # print(hit)
                #
                # while True:
                #     if hit:
                #         time_since_click = pygame.time.get_ticks() - hit
                #         print(time_since_click)
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player2.rect.x, 400))
                #         if time_since_click > 1000:
                #             break

                effect_punch.play(0)
                print("slag")
                player2.hp -= 10
                print(f"HP PLAYER 2: {player2.hp}")
        if keys.key == pygame.K_DOWN:
            if collision(player1, player2) == True:
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player2.rect.x, 400))
                print("spark")
                effect_KICK.play(0)
                player2.hp -= 10
                print(f"HP PLAYER 2: {player2.hp}")
        # fighter2 slag och spark
        if keys.key == pygame.K_w:
            if collision(player1, player2) == True:
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player1.rect.x, 400))
                effect_punch.play(0)
                print("slag")
                player1.hp -= 10
                print(f"HP PLAYER 1: {player1.hp}")

        if keys.key == pygame.K_s:
            if collision(player1, player2) == True:
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player1.rect.x, 400))
                effect_KICK.play(0)
                print("spark")
                player1.hp -= 10
                print(f"HP PLAYER 1: {player1.hp}")


def player_dead(player1, player2):
    if player1.hp == 0:
        player1.dead = True
        effect_dead.play(0)

    if player2.hp == 0:
        player2.dead = True
        effect_dead.play(0)


def fight(current_match):
    fight_music()
    global keys
    running = True
    player1_pics(player1, current_match)
    player1.rect.x = 720
    player1.rect.y = 500

    player2_pics(player2, current_match)
    player2.rect.x = 60
    player2.rect.y = 500
    while running:

        player_bars(1, current_match)
        player_bars(2, current_match)
        player_dead(player1, player2)
        if player1.dead == True:
            winner = matchup[current_match][0]
            loser = matchup[current_match][1]
        if player2.dead == True:
            winner = matchup[current_match][1]
            loser = matchup[current_match][0]
        if player1.dead == True or player2.dead == True:
            # återställer hp för båda
            player1.hp = 100
            player2.hp = 100
            # återställer tillstånd
            player1.dead = False
            player2.dead = False
            player1.frame = 0
            player2.frame = 0

            # om en spelare är död returnera vinnarens nummer
            # låt stå, funkar trots varning
            return winner, loser

        healthbar(player1, player2)
        fps_clock.tick(fps)
        screen.fill(black)
        screen.blit(bg_image[0], (0, 0))
        player_list.draw(screen)
        audience(current_match)
        for keys in pygame.event.get():
            if keys.type == pygame.QUIT:
                sys.exit()
            punch_and_kick(current_match)
        player_movement(player1, player2)
