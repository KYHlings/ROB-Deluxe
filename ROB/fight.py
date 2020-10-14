import pygame
import os
from ROB.main_menu import main_menu
from ROB.lobby import lobby

os.environ["SDL_VIDEO_CENTERED"] = "1"
black = (0, 0, 0)
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = [pygame.image.load('pics//arena_bakgrund_0.png'),pygame.image.load('pics//arena_bakgrund_1.png')]

fps_clock = pygame.time.Clock()
fps = 120

#TODO loopa bakrundsbilderna
screen.blit(bg_image[0],(0, 0))
screen.blit(bg_image[1],(0, 0))


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


def player1_pics(self):
    self.images = []
    # images = [pygame.image.load("pics//walking_right_2.png"),pygame.image.load("pics//walk_right_3.png")]
    for i in range(1, 3):
        img = pygame.image.load(os.path.join('pics', 'walking_right_' + str(i) + '.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(black)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)


player1 = Player()
player1_pics(player1)
player1.rect.x = 720
player1.rect.y = 200
player2 = Player()
player1_pics(player2)
player2.rect.x = 60
player2.rect.y = 200

player_list = pygame.sprite.Group()
player_list.add(player1, player2)


def collision(player1, player2):
    col = pygame.sprite.collide_rect(player1, player2)
    if col == True:
        return True


def player_movement(player1, player2):
    # Grund inställningar
    player1.rect.y += player1.vel
    player2.rect.y += player2.vel
    if player1.rect.y == 500:
        player1.vel = 0
    if player2.rect.y == 500:
        player2.vel = 0
    keys = pygame.key.get_pressed()


    # FIGHTER 1
    if keys[pygame.K_LEFT] and player1.rect.x > player1.vel:
        player1.left = True
        player1.right = False
        if collision(player1, player2) == True:
            if player1.left == True:
                player1.rect.x += 5
                #TODO det finns en bug där man flyger utanför skärmen om spelarna kolliderar och går åt ett håll tillsammans
        player1.rect.x -= 1
        player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)
        player1.frame += 1
        if player1.frame == 2:
            player1.frame = 0

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

    # hopp
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



# run order
main_menu()
lobby()
# pygame.mixer.music.stop()
# pygame.mixer.music.load('music//fight_music.ogg')
# pygame.mixer.music.play(-1)

def punch_and_kick():
    # fighter2 slag och spark
        if keys.type == pygame.KEYDOWN:
            if keys.key == pygame.K_UP:
                if collision(player1, player2) == True:
                    print("slag")
                    player1.hp -= 10
                    print(player1.hp)
            if keys.key == pygame.K_DOWN:
                if collision(player1, player2) == True:
                    print("spark")
                    player1.hp -= 10
                    print(player1.hp)

            #fighter1 slag och spark
            if keys.type == pygame.K_w:
                if collision(player1, player2) == True:
                    print("slag")
                    player2.hp -= 10
                    print(player2.hp)
            if keys.type == pygame.K_s:
                if collision(player2, player2) == True:
                    print("spark")
                    player2.hp -= 10
                    print(player2.hp)



running = True
while running:
    fps_clock.tick(fps)
    screen.fill(black)
    screen.blit(bg_image[0], (0, 0))
    player_list.draw(screen)
    for keys in pygame.event.get():
        if keys.type == pygame.QUIT:
            running = False
        punch_and_kick()
    player_movement(player1, player2)
    pygame.display.update()

