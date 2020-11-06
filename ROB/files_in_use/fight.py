import sys
import pygame
import os

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
bg_image = [pygame.image.load('images/backgrounds/arena_bakgrund_0.png'), pygame.image.load('images/backgrounds/arena_bakgrund_1.png')]
hannes = pygame.image.load('images/sprites/walking_right_purple_0.png')
berit = pygame.image.load('images/sprites/walking_right_yellow_0.png')
sune = pygame.image.load('images/sprites/walking_right_0.png')
bob = pygame.image.load('images/sprites/walking_right_green_0.png')
matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"],
           ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"],
           ["Boxare Bob", "Bråkiga Berit"]]

# tar current_match som indata i funktionen audience
def audience(current_match, hannes, berit, sune, bob):
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


# Todo - Skapa en ny modul för alla musikfiler
# ljudeffekter
effect_punch = pygame.mixer.Sound('sound_and_music/sound/PUNCH.wav')
effect_dead = pygame.mixer.Sound('sound_and_music/sound/Wilhelm_Scream.ogg')
effect_KICK = pygame.mixer.Sound('sound_and_music/sound/KICK.wav')

# fps
fps_clock = pygame.time.Clock()
fps = 120

# TODO loopa bakrundsbilderna så att bilden ser "rörlig" ut
screen.blit(bg_image[0], (0, 0))
screen.blit(bg_image[1], (0, 0))
font = pygame.font.SysFont("Arial", 15)

#gör en funktion för musiken i fightrutan
def fight_music():
    #stoppar föregående låt
    pygame.mixer.music.stop()
    # laddar in fight-låten
    pygame.mixer.music.load('sound_and_music/music/fight_music.ogg')
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
        # skapar vi en variabel för karaktärernas health points
        self.hp = 100
        # skapar en variabel som bestämmer om spelaren lever eller inte
        self.dead = False

# skapar en funktion med self och match som indata som gör att rätt bild laddas in till rätt match
def player_left_pics(self, match):
    # Sune är röd, Bob är grön, Berit är gul, Hannes är lila
    # Sune vs Bob
    if match == 0:
        # Återställer self.images listan så att den blir tom inför nästa fight
        self.images = []
        # skapar en loop som går mellan siffrorna 0-2
        for i in range(1, 3):
            # vi skapar en variabel img som lagrar 3 st bilder (str(i) loopar igenom namnen 0-2)
            img = pygame.image.load(f'images/sprites/walking_right_{str(i)}.png')
            # Lägger variabeln img i den tomma listan images
            self.images.append(img)
            # skapar ny variabel sätter värdet av första bilden (index 0) i listan self.images
            self.image = self.images[0]
            # vi sätter en rektangel som är samma storlek som den första bilden
            self.rect = self.image.get_rect()



    # Berit vs Hannes
    if match == 1:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images/sprites/walking_right_yellow_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    # Sune vs Berit
    if match == 2:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images//walking_right_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    # Bob vs Hannes
    if match == 3:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images//walking_right_green_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


    # Sune vs Hannes
    if match == 4:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images//walking_right_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    # Bob vs Berit
    if match == 5:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images//walking_right_green_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


def player_right_pics(self, match):
    # Sune är röd, Bob är grön, Berit är gul, Hannes är lila
    # Sune vs Bob

    # TODO kan möjligvis krasha på index error för att player_right.frame är 2, håll koll vid testning.
    if match == 0:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images/sprites/walking_right_green_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            # Vänder den högra spelaren så att han kollar åt vänster
            player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Berit vs Hannes

    if match == 1:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images/sprites/walking_right_purple_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Sune vs Berit

    if match == 2:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images/sprites/walking_right_yellow_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Bob vs Hannes

    if match == 3:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images/sprites/walking_right_purple_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Sune vs Hannes

    if match == 4:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images/sprites/walking_right_purple_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Bob vs Berit
    if match == 5:
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(f'images/sprites/walking_right_yellow_{str(i)}.png')
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

# Gör en instans av klassen Player och lagrar den i variabeln player_right. Sätter grundinställningarna på player_right. Gör så att vi kan ändra saker åt varje gubbe
player_right = Player()
# Sätter player_right till 100 hp
player_right.hp = 100
player_left = Player()
player_left.hp = 100

# spawnar spelare


# lägger alla spelare i en sprite grupp
player_list = pygame.sprite.Group()
player_list.add(player_right, player_left)

# skapar en funktion med which och current_match som indata
def player_name_hp_bar(which, current_match):
    font = pygame.font.SysFont("Arial", 20)
    # bestämmer vart spelarnas namn skall visas. Spelarnas namn ändras efter varje match genom att kolla i matchup listan
    if which == 1:
        screen.blit(font.render(f"{matchup[current_match][0]}", True, (255, 255, 255)), (50, 20))
    if which == 2:
        screen.blit(font.render(f"{matchup[current_match][1]}", True, (255, 255, 255)), (550, 20))

# skapar en funktion för health bar med båda spelarna som indata
def healthbar(player_right, player_left):
    # om player_right eller player 2's hp är större än -10 så målas rektanglar upp för healtbarsen.
    if player_right.hp > -10:
        bg_bar1 = pygame.Rect(550, 50, 200, 50)
        hp_bar1 = pygame.Rect(550, 50, 200 * (player_right.hp * 0.01), 50)
        pygame.draw.rect(screen, (255, 0, 0), bg_bar1)
        pygame.draw.rect(screen, (0, 255, 0), hp_bar1)
    if player_left.hp > -10:
        bg_bar2 = pygame.Rect(50, 50, 200, 50)
        hp_bar2 = pygame.Rect(50, 50, 200 * (player_left.hp * 0.01), 50)
        pygame.draw.rect(screen, (255, 0, 0), bg_bar2)
        pygame.draw.rect(screen, (0, 255, 0), hp_bar2)
    pygame.display.update()

# Skapar en funktion med player 1 och player 2 som indata som kollar om kollision har skett
def collision(player_right, player_left):
    # kollar om kollision har skett
    col = pygame.sprite.collide_rect(player_right, player_left)
    if col == True:
        return True

# Skapar en funktion med player 1 och player 2 som indata
def player_movement(player_right, player_left):
    # Gör så att player 1 och player 2 faller ner efter hopp
    player_right.rect.y += player_right.vel
    player_left.rect.y += player_left.vel
    # Skapar variabeln keys som upptäcker ifall en tangent är nedtryckt
    keys = pygame.key.get_pressed()

    # TODO det finns en bug där man flyger utanför skärmen om spelarna kolliderar och går åt ett håll tillsammans
    # FIGHTER 1
    # vänster
    # Skapar en if-sats som ska göra att vänster pil-tangent tar gubben åt vänster. Gubben kommer aldrig utanför skärmens vänstra kant (0 på x-axeln)
    if keys[pygame.K_LEFT] and player_right.rect.x > 0:
        # Gäller när vänster pil-tangent är nedtryckt
        player_right.left = True
        player_right.right = False
        # Kollar ifall player 1 och player 2 kolliderar
        if collision(player_right, player_left) == True:
            # Gör att spelaren åker tillbaka 5 pixlar vid kollision
            if player_right.left == True:
                player_right.rect.x += 5
        # Player 1's x-värde ändras med -1 pixel när han går åt vänster
        player_right.rect.x -= 1
        # Vänder bilden åt vänster när player 1 går åt vänster
        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)
        # Gör så bilderna plussas på och animation skapas av att gubben går till vänster
        player_right.frame += 1
        # Om man plussat upp till index 2 så går den tillbaka till 0 (0, 1, 2...0, 1, 2...)
        if player_right.frame == 2:
            player_right.frame = 0

    # höger
    # Skapar en if-sats som ska göra att höger pil-tangent tar gubben åt höger.
    # Gubben kommer aldrig utanför skärmens högra kant.
    if keys[pygame.K_RIGHT] and player_right.rect.x < screen_width - 40:
        # Gäller när höger pil-tangent är nedtryckt
        player_right.left = False
        player_right.right = True
        if collision(player_right, player_left) == True:
            if player_right.right == True:
                # studsar tillbaka efter kollision
                player_right.rect.x -= 5
        # Player1's x-värde ändras med 1 pixel när man går åt höger
        player_right.rect.x += 1
        player_right.frame += 1
        if player_right.frame == 2:
            player_right.frame = 0
        # Eftersom bilderna vi har laddat in redan är åt höger så behöver vi ej flippa
        player_right.image = player_right.images[player_right.frame]
# TODO - Gör så att man inte kan flyga
    # HOPP
    # Om den högra ctrl-tangenten är nedtryckt
    if keys[pygame.K_UP]:
        # hoppets höjd
        player_right.rect.y -= 15
        # dragningskraft
        player_right.vel = 3
        # invisible border max hopphöjd
        if player_right.rect.y < 200:
            # ändrar dragningskraften till 20 pixlar
            player_right.vel = 20
    # lägsta punkt
    if player_right.rect.y > 500:
        player_right.rect.y = 500

    # FIGTER 2
    # vänster
    if keys[pygame.K_a] and player_left.rect.x > player_left.vel:
        player_left.left = True
        player_left.right = False
        if collision(player_right, player_left) == True:
            if player_left.left == True:
                player_left.rect.x += 5
        player_left.rect.x -= 1
        player_left.image = pygame.transform.flip(player_left.images[player_left.frame], True, False)
        player_left.frame += 1
        if player_left.frame == 2:
            player_left.frame = 0

    # höger
    if keys[pygame.K_d] and player_left.rect.x < screen_width - 40:
        player_left.left = False
        player_left.right = True
        if collision(player_right, player_left) == True:
            if player_left.right == True:
                player_left.rect.x -= 5
        player_left.rect.x += 1
        player_left.frame += 1
        if player_left.frame == 2:
            player_left.frame = 0
        player_left.image = player_left.images[player_left.frame]

    # HOPP
    if keys[pygame.K_w]:
        # hoppets höjd
        player_left.rect.y -= 15
        # dragningskraft
        player_left.vel = 3
        # invisible border max hopphöjd
        if player_left.rect.y < 200:
            player_left.vel = 20
    # lägsta punkt
    if player_left.rect.y > 500:
        player_left.rect.y = 500


def punch_and_kick():
    # TODO - Försök fixa så att man kan göra airstrikes med spark de hade vart nice å se
    # kollar om en knapp är nedtryckt
    if keys.type == pygame.KEYDOWN:
        # fighter1 slag och spark
        # Om man trycker ner tangenten pil upp
        if keys.key == pygame.K_UP:
            # Om det sker en collision mellan player_right och player_right samt att man trycker på pil upp så dyker texten "hit" upp på skärmen, en ljudeffekt spelas och player_right.hp minskas med 10
            if collision(player_right, player_left) == True:
                # TODO - Få 'hit' att stanna på skärmen längre än att bara blinka till / lägga till någon bild eller animation när man slår
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player_left.rect.x, 400))
                effect_punch.play(0)
                print("slag")
                player_left.hp -= 10
                print(f"HP PLAYER 2: {player_left.hp}")
        if keys.key == pygame.K_DOWN:
            if collision(player_right, player_left) == True:
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player_left.rect.x, 400))
                print("spark")
                effect_KICK.play(0)
                player_left.hp -= 10
                print(f"HP PLAYER 2: {player_left.hp}")
        # fighter2 slag och spark
        if keys.key == pygame.K_w:
            if collision(player_right, player_left) == True:
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player_right.rect.x, 400))
                effect_punch.play(0)
                print("slag")
                player_right.hp -= 10
                print(f"HP PLAYER 1: {player_right.hp}")

        if keys.key == pygame.K_s:
            if collision(player_right, player_left) == True:
                screen.blit(font.render("Hit!", True, (255, 255, 255)), (player_right.rect.x, 400))
                effect_KICK.play(0)
                print("spark")
                player_right.hp -= 10
                print(f"HP PLAYER 1: {player_right.hp}")

# Skapar en funktion med player_right och player_right som indata
def player_dead(player_right, player_left):
    # Om player_right når 0 eller mindre i hp så dör han och en ljudeffekt spelas upp.
    if player_right.hp <= 0:
        player_right.dead = True
        effect_dead.play(0)

    if player_left.hp <= 0:
        player_left.dead = True
        effect_dead.play(0)

# Skapar fight-funktionen med current_match som indata
def fight(current_match):
    # Anropar funktionen fight_music som spelar upp fight-låten.
    fight_music()
    # Gör variabeln keys tillgänglig i hela koden
    global keys
    running = True
    # Anropar funktionen player_right_pics som ger player_right rätt bildinställningar för nuvarande match
    player_right_pics(player_right, current_match)
    # Anger startpostionen för player_right
    player_right.rect.x = 720
    player_right.rect.y = 500
    # Anropar funktionen player_left_pics som ger player_right rätt bildinställningar för nuvarande match
    player_left_pics(player_left, current_match)
    # Anger startpositionen för player_right
    player_left.rect.x = 60
    player_left.rect.y = 500

    # Så länge running är True kommer spelet köras
    while running:

        # Anropar en funktion som skriver ut spelare 1 och 2's namn ovanför hp-baren, namnen är beroende av vilken match som körs via current_match
        player_name_hp_bar(1, current_match)
        player_name_hp_bar(2, current_match)
        #Anropar funktionen player_dead med player_right och player 2 som indata
        player_dead(player_right, player_left)
        # Om det är True att player_right är död
        if player_right.dead == True:
            # Då blir vinnaren player_left i den nuvarande matchen via matchup listan och förloraren blir player_left i samma match
            winner = matchup[current_match][0]
            loser = matchup[current_match][1]
        # Om det är True att player_right är död
        if player_left.dead == True:
            # Då blir vinnaren player_right i den nuvarande matchen via matchup listan och förloraren blir player_right i samma match
            winner = matchup[current_match][1]
            loser = matchup[current_match][0]
        # Om någon av spelarna är död
        if player_right.dead == True or player_left.dead == True:
            # återställer hp för båda
            player_right.hp = 100
            player_left.hp = 100
            # återställer tillstånd inför nästa match
            player_right.dead = False
            player_left.dead = False
            player_right.frame = 0
            player_left.frame = 0

            # om en spelare är död returnera vinnarens nummer
            # låt stå, funkar trots varning
            return winner, loser
        # Anropar healthbar-funktionen med player_right och player_left som indata
        # Får fram healthbaren på skärmen
        healthbar(player_right, player_left)
        # Sätter fps till det som angivits tidigare i fps-variabeln. Fps = frames per second
        fps_clock.tick(fps)
        # Fyller skärmen med svart färg
        screen.fill(black)
        # Målar upp en bakgrundsbild som täcker hela skärmen
        screen.blit(bg_image[0], (0, 0))
        # Ritar ut player_right och player_left på skärmen
        player_list.draw(screen)
        # Anropar funktionen audience
        audience(current_match, hannes, berit, sune, bob)
        # Anropar funktionen player_movement
        player_movement(player_right, player_left)
        # Loopar igenom alla möjliga events i pygame som lagras keys
        for keys in pygame.event.get():
            # Om keys.type är lika med pygame.QUIT så ska programmet stängas ned
            if keys.type == pygame.QUIT:
                sys.exit()
            # Kollar knapptryckningar i punch_and_kick-funktionen
            punch_and_kick()


