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
bg_image = pygame.image.load('images/backgrounds/arena_background.jpg')
bg_image = pygame.transform.scale(bg_image, (800, 600))
# hannes = pygame.image.load('images/sprites/hannes/walking_right_purple_0.png').convert_alpha()
# berit = pygame.image.load('images/sprites/berit/walking_right_yellow_0.png').convert_alpha()
# sune = pygame.image.load('images/sprites/sune/walking_right_0.png').convert_alpha()
# bob = pygame.image.load('images/sprites/green1.png').convert_alpha()
matchup = [["Slaktar Sune", "Boxare Bob"], ["Bråkiga Berit", "Hänsynslöse Hannes"], ["Slaktar Sune", "Bråkiga Berit"],
           ["Boxare Bob", "Hänsynslöse Hannes"], ["Slaktar Sune", "Hänsynslöse Hannes"],
           ["Boxare Bob", "Bråkiga Berit"]]

# tar current_match som indata i funktionen audience
# def audience(current_match, hannes, berit, sune, bob):
#     # bestämmer vem som ska stå i publiken beroende på vilken siffra current_match blir
#     if current_match == 0:
#         screen.blit(hannes, (40, 170))
#         screen.blit(berit, (70, 170))
#     if current_match == 1:
#         screen.blit(sune, (40, 170))
#         screen.blit(bob, (70, 170))
#     if current_match == 2:
#         screen.blit(hannes, (40, 170))
#         screen.blit(bob, (70, 170))
#     if current_match == 3:
#         screen.blit(sune, (40, 170))
#         screen.blit(berit, (70, 170))
#     if current_match == 4:
#         screen.blit(bob, (40, 170))
#         screen.blit(berit, (70, 170))
#     if current_match == 5:
#         screen.blit(sune, (40, 170))
#         screen.blit(hannes, (70, 170))


# Todo - Skapa en ny modul för alla musikfiler
# ljudeffekter
effect_punch = pygame.mixer.Sound('sound_and_music/sound/PUNCH.wav')
effect_dead = pygame.mixer.Sound('sound_and_music/sound/Wilhelm_Scream.ogg')
effect_KICK = pygame.mixer.Sound('sound_and_music/sound/KICK.wav')

# fps
fps_clock = pygame.time.Clock()
fps = 9999

# TODO loopa bakrundsbilderna så att bilden ser "rörlig" ut
screen.blit(bg_image, (0, 0))

font = pygame.font.SysFont("Arial", 15)


# gör en funktion för musiken i fightrutan
def fight_music():
    # stoppar föregående låt
    pygame.mixer.music.stop()
    # laddar in fight-låten
    pygame.mixer.music.load('sound_and_music/music/rob_fight.mp3')
    # spelar fightlåten om och om igen
    pygame.mixer.music.play(-1)


# gör en klass som heter player så tar vi pygame.sprite.Sprite som indata som bestämmer att objektet är en sprite
class Player(pygame.sprite.Sprite):
    # sätter grundinställningar för varje Player som skapas
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # bestämmer hoppets hastighet för gubbarnas rörelser i pixlar
        self.vel = 40
        # bestämmer vilken bild som ska visas i images listan över spelarens olika bilder
        self.frame = 0
        # bestämmer vänster och höger riktning
        self.left = False
        self.right = False
        # skapar en variabel för spelarens storlek som ändras senare
        self.rect = (0, 0, 0, 0)
        # skapar en tom lista där vi senare ska lagra dom bilder karaktärerna ska ha
        self.images = []
        self.fight_images = []
        # skapar vi en variabel för karaktärernas health points
        self.hp = 100
        # skapar en variabel som bestämmer om spelaren lever eller inte
        self.dead = False
        self.jumping = False
        self.recently_hit = False
        self.time_hit = None
        self.ascending = False
        self.attacking = False
        self.attack_time = 0

    def hoppi_ti_hopp(self):
        if self.ascending:
            self.rect.y -= 7
            if self.rect.y < 300:
                self.ascending = False
        else:
            if self.rect.y >= 450:
                self.jumping = False


# skapar en funktion med self och match som indata som gör att rätt bild laddas in till rätt match
def player_left_pics(self, match):
    # Sune är röd, Bob är grön, Berit är gul, Hannes är lila
    # Sune vs Bob
    if match == 0:
        # Återställer self.images listan så att den blir tom inför nästa fight
        # skapar en loop som går mellan siffrorna 0-2
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/sune/red{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/sune/red_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/sune/red_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

    # Berit vs Hannes
    if match == 1:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/berit/yellow{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/berit/yellow_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/berit/yellow_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

    # Sune vs Berit
    if match == 2:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/sune/red{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/sune/red_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/sune/red_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

    # Bob vs Hannes
    if match == 3:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/bob/green{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/bob/green_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/bob/green_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

    # Sune vs Hannes
    if match == 4:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/sune/red{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/sune/red_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/sune/red_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

    # Bob vs Berit
    if match == 5:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/bob/green{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/bob/green_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/bob/green_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()


def player_right_pics(self, match):
    # Sune är röd, Bob är grön, Berit är gul, Hannes är lila
    # Sune vs Bob

    # TODO kan möjligvis krasha på index error för att player_right.frame är 2, håll koll vid testning.
    if match == 0:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/bob/green{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/bob/green_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/bob/green_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Berit vs Hannes

    if match == 1:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/hannes/blue{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/hannes/blue_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/hannes/blue_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Sune vs Berit

    if match == 2:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/berit/yellow{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/berit/yellow_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/berit/yellow_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Bob vs Hannes

    if match == 3:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/hannes/blue{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/hannes/blue_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/hannes/blue_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Sune vs Hannes

    if match == 4:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/hannes/blue{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/hannes/blue_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/hannes/blue_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)

    # Bob vs Berit
    if match == 5:
        self.images = []
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 3 or i == 4:
                j = 1
            if i == 5 or i == 6 or i == 7 or i == 8:
                j = 2
            if i == 9 or i == 10 or i == 11 or i == 12:
                j = 3
            if i == 13 or i == 14 or i == 15 or i == 16:
                j = 4
            img = pygame.image.load(f'images/sprites/berit/yellow{j}.png').convert_alpha()
            self.mask = pygame.mask.from_surface(img)
            self.images.append(img)
            self.image = self.images[0]
            self.fight_images = [pygame.image.load(f'images/sprites/berit/yellow_windup.png').convert_alpha(),
                                 pygame.image.load(f'images/sprites/berit/yellow_fight.png').convert_alpha()]
            self.rect = self.image.get_rect()

        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)


# Gör en instans av klassen Player och lagrar den i variabeln player_right. Sätter grundinställningarna på
# player_right. Gör så att vi kan ändra saker åt varje gubbe
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
    # bestämmer vart spelarnas namn skall visas. Spelarnas namn ändras efter varje match genom att kolla i matchup
    # listan
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
# def collision(player_right, player_left):
#     # kollar om kollision har skett
#     col = pygame.sprite.collide_rect(player_right, player_left)
#     if col:
#         return True
def collision(player_1, player_2):
    # Checks collision between mobs and player
    (mx, my) = (player_1.rect[0], player_1.rect[1])
    px = mx - player_2.rect[0]
    py = my - player_2.rect[1]
    overlap = player_2.mask.overlap(player_1.mask, (px, py))
    if overlap:
        return True


# Skapar en funktion med player 1 och player 2 som indata
def player_movement(player_right, player_left):
    # Gör så att player 1 och player 2 faller ner efter hopp
    player_right.rect.y += player_right.vel
    player_left.rect.y += player_left.vel
    # Skapar variabeln keys som upptäcker ifall en tangent är nedtryckt
    keys = pygame.key.get_pressed()

    # TODO det finns en bug där man flyger utanför skärmen om spelarna kolliderar och går åt ett håll tillsammans
    #  FIGHTER 1 vänster Skapar en if-sats som ska göra att vänster pil-tangent tar gubben åt vänster. Gubben kommer
    #  aldrig utanför skärmens vänstra kant (0 på x-axeln)
    if keys[pygame.K_LEFT] and player_right.rect.x > 0:
        # Gäller när vänster pil-tangent är nedtryckt
        player_right.left = True
        player_right.left += player_right.vel
        player_right.right = False
        # Kollar ifall player 1 och player 2 kolliderar
        if collision(player_right, player_left):
            # Gör att spelaren åker tillbaka 5 pixlar vid kollision
            if player_right.left:
                player_right.rect.x += 5
        # Player 1's x-värde ändras med -1 pixel när han går åt vänster
        player_right.rect.x -= 1
        # Vänder bilden åt vänster när player 1 går åt vänster
        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)
        # Gör så bilderna plussas på och animation skapas av att gubben går till vänster
        player_right.frame += 1
        # Om man plussat upp till index 2 så går den tillbaka till 0 (0, 1, 2...0, 1, 2...)
        if player_right.frame == 16:
            player_right.frame = 0

    # höger
    # Skapar en if-sats som ska göra att höger pil-tangent tar gubben åt höger.
    # Gubben kommer aldrig utanför skärmens högra kant.
    if keys[pygame.K_RIGHT] and player_right.rect.x < screen_width - 40:
        # Gäller när höger pil-tangent är nedtryckt
        player_right.left = False
        player_right.right = True
        if collision(player_right, player_left):
            if player_right.right:
                # studsar tillbaka efter kollision
                player_right.rect.x -= 5
        # Player1's x-värde ändras med 1 pixel när man går åt höger
        player_right.rect.x += 1
        player_right.frame += 1
        if player_right.frame == 16:
            player_right.frame = 0
        # Eftersom bilderna vi har laddat in redan är åt höger så behöver vi ej flippa
        player_right.image = player_right.images[player_right.frame]
    # TODO - Gör så att man inte kan flyga
    if player_right.rect.y > 450:
        if keys[pygame.K_UP]:
            player_right.jumping = True
            player_right.ascending = True
            # hoppets höjd
            # dragningskraft
            player_right.vel = 3
            # invisible border max hopphöjd
            if player_right.rect.y < 100:
                player_right.vel = 20

        # lägsta punkt
    player_right.hoppi_ti_hopp()
    if player_right.rect.y > 450:
        player_right.rect.y = 450

    if keys[pygame.K_RCTRL]:
        player_right.attacking = True

    if player_left.recently_hit:
        player_left.recently_hit = player_hit_left(player_left.time_hit)
    # FIGTER 2
    # vänster
    if keys[pygame.K_a] and player_left.rect.x > player_left.vel:
        player_left.left = True
        player_left.right = False
        if collision(player_right, player_left):
            if player_left.left:
                player_left.rect.x += 5
        player_left.rect.x -= 1
        player_left.image = pygame.transform.flip(player_left.images[player_left.frame], True, False)
        player_left.frame += 1
        if player_left.frame == 16:
            player_left.frame = 0

    # höger
    if keys[pygame.K_d] and player_left.rect.x < screen_width - 40:
        player_left.left = False
        player_left.right = True
        if collision(player_right, player_left):
            if player_left.right:
                player_left.rect.x -= 5
        player_left.rect.x += 1
        player_left.frame += 1
        if player_left.frame == 16:
            player_left.frame = 0
        player_left.image = player_left.images[player_left.frame]

    # HOPP
    if player_left.rect.y > 450:
        if keys[pygame.K_w]:
            player_left.jumping = True
            player_left.ascending = True
            # hoppets höjd
            # dragningskraft
            player_left.vel = 3
            # invisible border max hopphöjd
            if player_left.rect.y < 100:
                player_left.vel = 20
        # lägsta punkt
    player_left.hoppi_ti_hopp()
    if player_left.rect.y > 450:
        player_left.rect.y = 450

    if keys[pygame.K_LCTRL]:
        player_left.attacking = True

    if player_right.attacking:
        if player_right.attack_time > 25:
            player_right.attacking = False
            player_right.attack_time = 0
        if collision(player_left, player_right):
            player_left.recently_hit = True
            player_left.time_hit = pygame.time.get_ticks()
            player_left.rect.x -= 50

            effect_punch.play(0)
            player_left.hp -= 10

    if player_left.attacking:
        if player_left.attack_time > 25:
            player_left.attacking = False
            player_left.attack_time = 0
        if collision(player_right, player_left):
            player_right.recently_hit = True
            player_right.time_hit = pygame.time.get_ticks()
            player_right.rect.x += 50

            effect_punch.play(0)
            player_right.hp -= 10

    if player_right.recently_hit:
        player_right.recently_hit = player_hit_right(player_right.time_hit)


def player_hit_right(hit_timer):
    if pygame.time.get_ticks() - hit_timer >= 1500:
        return False
    else:
        screen.blit(font.render("Hit!", True, (255, 255, 255)), (player_right.rect.x, 400))
        return True


def player_hit_left(hit_timer):
    if pygame.time.get_ticks() - hit_timer >= 1500:
        return False
    else:
        screen.blit(font.render("Hit!", True, (255, 255, 255)), (player_left.rect.x, 400))
        return True


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
    player_right.rect.x = 680
    player_right.rect.y = 450
    # Anropar funktionen player_left_pics som ger player_right rätt bildinställningar för nuvarande match
    player_left_pics(player_left, current_match)
    # Anger startpositionen för player_right
    player_left.rect.x = 0
    player_left.rect.y = 450

    # Så länge running är True kommer spelet köras
    while running:

        # Anropar en funktion som skriver ut spelare 1 och 2's namn ovanför hp-baren, namnen är beroende av vilken
        # match som körs via current_match
        player_name_hp_bar(1, current_match)
        player_name_hp_bar(2, current_match)
        # Anropar funktionen player_dead med player_right och player 2 som indata
        player_dead(player_right, player_left)
        # Om det är True att player_right är död
        if player_right.dead:
            # Då blir vinnaren player_left i den nuvarande matchen via matchup listan och förloraren blir player_left
            # i samma match
            winner = matchup[current_match][0]
            loser = matchup[current_match][1]
        # Om det är True att player_right är död
        if player_left.dead:
            # Då blir vinnaren player_right i den nuvarande matchen via matchup listan och förloraren blir
            # player_right i samma match
            winner = matchup[current_match][1]
            loser = matchup[current_match][0]
        # Om någon av spelarna är död
        if player_right.dead or player_left.dead:
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
        screen.blit(bg_image, (0, 0))
        # Ritar ut player_right och player_left på skärmen

        # print(player_left.jumping)
        if player_left.jumping:
            player_left.image = player_left.images[4]

        if player_right.jumping:
            player_right.image = player_right.images[4]
            player_right.image = pygame.transform.flip(player_right.image, True, False)
        # print(player_right.attack_time)
        if player_right.attacking:
            if player_right.attack_time < 8 or player_right.attacking > 20:
                player_right.image = player_right.fight_images[0]
            else:
                player_right.image = player_right.fight_images[1]
            player_right.image = pygame.transform.flip(player_right.image, True, False)
            player_right.attack_time += 1

        if player_left.attacking:
            if player_left.attack_time < 8 or player_left.attacking > 20:
                player_left.image = player_left.fight_images[0]
            else:
                player_left.image = player_left.fight_images[1]
            player_left.attack_time += 1
            # print(player_right.attack_time)
        player_list.draw(screen)
        # Anropar funktionen audience
        # audience(current_match, hannes, berit, sune, bob)
        # Anropar funktionen player_movement
        player_movement(player_right, player_left)
        # Loopar igenom alla möjliga events i pygame som lagras keys
        for keys in pygame.event.get():
            # Om keys.type är lika med pygame.QUIT så ska programmet stängas ned
            if keys.type == pygame.QUIT:
                sys.exit()
