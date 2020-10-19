import pygame
import os


# grundinställningar

class Fight():
    def __init__(self, player_right, player_left):

        os.environ["SDL_VIDEO_CENTERED"] = "1"
        self.black = (0, 0, 0)
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_image = [pygame.image.load('pics//arena_bakgrund_0.png'), pygame.image.load('pics//arena_bakgrund_1.png')]

        # TODO loopa bakrundsbilderna
        self.screen.blit(self.bg_image[0], (0, 0))
        self.screen.blit(self.bg_image[1], (0, 0))

        # spawnar spelare
        player_right.player_right = Player()
        player1_pics(player_right.player_right)
        player_right.player_right.rect.x = 720
        player_right.player_right.rect.y = 200
        player_left.player_left = Player()
        player1_pics(player_left.player_left)
        player_left.player_left.rect.x = 60
        player_left.player_left.rect.y = 200

        # lägger alla spelare i en sprite grupp
        self.player_list = pygame.sprite.Group()
        self.player_list.add(player_right.player_right, player_left.player_left)

# ljudeffekter
effect_punch = pygame.mixer.Sound('music//PUNCH.wav')
effect_dead = pygame.mixer.Sound('music//Wilhelm_Scream.ogg')
effect_KICK = pygame.mixer.Sound('music//KICK.mp3')

# fps
fps_clock = pygame.time.Clock()
fps = 120

f = Fight()


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # how many pixels the character is moving per action
        self.vel = 5
        self.frame = 0
        # stating left and right
        self.left = False
        self.right = False
        self.rect = (0, 0, 0, 0)
        self.images = []
        self.image = [pygame.image.load("pics//walking_right_2.png")]
        self.hp = 100


def player1_pics(player_right, self):
    self.images = []
    for i in range(1, 3):
        img = pygame.image.load(os.path.join('pics', 'walking_right_' + str(i) + '.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(f.black)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        player_right.player_right.image = pygame.transform.flip(player_right.player_right.images[player_right.player_right.frame], True, False)





def healthbar(player1, player2):
    if player1.hp > -10:
        bg_bar1 = pygame.Rect(550, 50, 200, 50)
        hp_bar1 = pygame.Rect(550, 50, 200*(player1.hp*0.01), 50)
        pygame.draw.rect(f.screen, (255, 0, 0), bg_bar1)
        pygame.draw.rect(f.screen, (0, 255, 0), hp_bar1)

    if player2.hp > -10:
        bg_bar2 = pygame.Rect(50, 50, 200, 50)
        hp_bar2 = pygame.Rect(50, 50, 200*(player2.hp*0.01), 50)
        pygame.draw.rect(f.screen, (255, 0, 0), bg_bar2)
        pygame.draw.rect(f.screen, (0, 255, 0), hp_bar2)
    pygame.display.update()


def collision(player1, player2):
    # kollar om kollision har skett
    col = pygame.sprite.collide_rect(player1, player2)
    if col == True:
        return True


def player_movement(player_right, player_left):

    # Grund inställningar för position
    player_right.rect.y += player_right.vel
    player_left.rect.y += player_left.vel
    if player_right.rect.y == 500:
        player_right.vel = 0
    if player_left.rect.y == 500:
        player_left.vel = 0
    keys = pygame.key.get_pressed()


# TODO det finns en bug där man flyger utanför skärmen om spelarna kolliderar och går åt ett håll tillsammans
# FIGHTER 1
    # vänster
    if keys[pygame.K_LEFT] and player_right.rect.x > player_right.vel:
        player_right.left = True
        player_right.right = False
        if collision(player_right, player_left) == True:
            if player_right.left == True:
                player_right.rect.x += 5
        player_right.rect.x -= 1
        player_right.image = pygame.transform.flip(player_right.images[player_right.frame], True, False)
        player_right.frame += 1
        if player_right.frame == 2:
            player_right.frame = 0

    # höger
    if keys[pygame.K_RIGHT] and player_right.rect.x < f.screen_width - 40:
        player_right.left = False
        player_right.right = True
        if collision(player_right, player_left) == True:
            if player_right.right == True:
                player_right.rect.x -= 5
        player_right.rect.x += 1
        player_right.frame += 1
        if player_right.frame == 2:
            player_right.frame = 0
        player_right.image = player_right.images[player_right.frame]

# HOPP
    if keys[pygame.K_RCTRL]:
        # hoppets höjd
        player_right.rect.y -= 15
        # dragningskraft
        player_right.vel = 3
        # invisible border max hopphöjd
        if player_right.rect.y < 200:
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
    if keys[pygame.K_d] and player_left.rect.x < f.screen_width - 40:
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
    if keys[pygame.K_SPACE]:
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


# run order
pygame.mixer.music.stop()
pygame.mixer.music.load('music//fight_music.ogg')
pygame.mixer.music.play(-1)


def punch_and_kick(keys, player_right, player_left):
    # kollar om en knapp är nedtryckt
    if keys.type == pygame.KEYDOWN:

        # fighter1 slag och spark
        if keys.key == pygame.K_w:
            if collision(player_right.player_right, player_left.player_left) == True:
                effect_punch.play(0)
                print("slag")
                player_left.player_left.hp -= 10
                print(f"HP PLAYER 2: {player_left.player_left.hp}")

        if keys.key == pygame.K_s:
            if collision(player_right.player_right, player_right.player_left) == True:
                print("spark")
                effect_KICK.play(0)
                player_left.player_left.hp -= 10
                print(f"HP PLAYER 2: {f.player_left.hp}")

        # fighter2 slag och spark
        if keys.key == pygame.K_UP:
            if collision(f.player_right, f.player_left) == True:
                effect_punch.play(0)
                print("slag")
                f.player_right.hp -= 10
                print(f"HP PLAYER 1: {f.player_right.hp}")
        if keys.key == pygame.K_DOWN:
            if collision(f.player_right, f.player_left) == True:
                print("spark")
                effect_KICK.play(0)
                f.player_right.hp -= 10
                print(f"HP PLAYER 1: {f.player_right.hp}")


def player_dead(player_right, player_left):
    dead = pygame.image.load("pics//player_dead.png")
    if player_left.hp == 0:
        f.screen.blit(dead)
        effect_dead.play(0)

    if player_right.hp == 0:
        f.screen.blit(dead)
        effect_dead.play(0)




def fight():

    running = True
    while running:
        healthbar(f.player_right, f.player_left)
        player_dead(f.player_right, f.player_left)
        fps_clock.tick(fps)
        f.screen.fill(f.black)
        f.screen.blit(f.bg_image[0], (0, 0))
        f.player_list.draw(f.screen)
        for keys in pygame.event.get():
            if keys.type == pygame.QUIT:
                running = False
            punch_and_kick(keys)
        player_movement(f.player_right, f.player_left)
        if f.player_right.hp == 0:
            return 1
        elif f.player_left.hp == 0:
            return 2



