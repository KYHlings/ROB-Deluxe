import pygame
import os


vec = pygame.math.Vector2
black=(0, 0, 0)
ani = 3
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))



fps_clock = pygame.time.Clock()
fps = 120




class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Dessa x ocy y värdena bestämmer vart på skärmen gubben spawnar
 #       self.x = start_x
  #      self.y = start_y
        # width and height values that decide the size of the character
  #      self.width = width
  #      self.height = height
        # how many pixels the character is moving per action
        self.vel = 5
        self.frame = 0
        # variables for the jumping mechanism
        self.is_jump = False
        self.jump_count = 10
        # counter for walking animation
        self.walk_count = 0
        # stating left and right
        self.left = False
        self.right = False
        self.standing = True
        self.rect = (0, 0, 0, 0)
        self.images = []
        self.image = [pygame.image.load("pics//walking_right_2.png")]
        self.grav = vec(0, 0.5)



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


player1 = Player()
player1_pics(player1)
player1.rect.x = 300
player1.rect.y = 150
player2 = Player()
player1_pics(player2)
player2.rect.x = 200
player2.rect.y = 150

player_list = pygame.sprite.Group()
player_list.add(player1, player2)


def collision(player1, player2):
    col = pygame.sprite.collide_rect(player1, player2)
    if col == True:
        print("hit")
        return True

def player_movement(player1, player2):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1.rect.x > player1.vel:
        player1.left = True
        player1.right = False
        if collision(player1, player2) == True:
            if player1.left == True:
                player1.rect.x += 5
                # det finns en bug där man flyger utanför skärmen om spelarna kolliderar och går åt ett håll tillsammans

        player1.rect.x -= 1
        player1.image = pygame.transform.flip(player1.images[player1.frame], True, False)
        player1.frame += 1
        if player1.frame == 2:
            player1.frame = 0
    elif keys[pygame.K_RIGHT] and player1.rect.x < screen_width - 40:
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

    if not player1.is_jump:
        if keys[pygame.K_SPACE]:
            player1.grav = vec(0, 0.5)
            player1.is_jump = True
            player1.left = False
            player1.right = False
    else:
        if player1.jump_count >= -10:
            neg_1 = 1
            if player1.jump_count < 0:
                neg_1 = -1
            # hastigeten på hoppet, höjd på hoppet,

            player1.rect.y -= (player1.jump_count ** 2) * 0.5 * neg_1
            player1.jump_count -= 1
        else:
            player1.is_jump = False
            player1.jump_count = 10
            player1.rect.y = 150
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
    elif keys[pygame.K_d] and player2.rect.x < screen_width - 40:
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

running = True
while running:
    fps_clock.tick(fps)
    pygame.display.update()
    screen.fill(black)
    player_list.draw(screen)
    for keys in pygame.event.get():
        if keys.type == pygame.QUIT:
            running = False
    player_movement(player1, player2)
