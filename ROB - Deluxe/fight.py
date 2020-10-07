import pygame

pygame.init()
# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
# parameters for the window size in pixels
screen_width = 1000
screen_height = 1000

# implementing a surface
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FIGHT")

casino_bg = pygame.image.load('pics//casino.png')
walk_right = [pygame.image.load('pics//walking_right_2.png')]
walk_left = [pygame.image.load('pics//walking_left_1.png')]
char = [pygame.image.load('pics//look_left.png'), pygame.image.load('pics//look_right.png')]
fps_clock = pygame.time.Clock()
fps = 60


class Player():
    def __init__(self, x, y, width, height):
        # starting x and y pos
        self.x = x
        self.y = y
        # x and y values that decide the size of the character
        self.width = width
        self.height = height
        # how many pixels the character is moving per action
        self.vel = 5
        self.vel_2 = 2
        # variables for the jumping mechanism
        self.is_jump = False
        self.jump_count = 10
        # counter for walking animation
        self.walk_count = 0
        # stating left and right
        self.left = False
        self.right = False
        self.standing = True
        self.rect = pygame.draw.rect(win, blue, (self.x, self.y, 29, 70))

    def check_collide(self, enemy):
        self.hitbox = pygame.draw.rect(win, black, (self.x, self.y, 29, 70))
        win.blit(self.hitbox)
        if self.hitbox.colliderect(enemy):
            print("HIT")


def draw_2(self, win):
        if self.walk_count + 1 >= 3:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.left:
                win.blit(char[0], (self.x, self.y))
            else:
                win.blit(char[1], (self.x, self.y))


# draws an invisible hitbox around our characters
def check_collide(self, enemy):
    hitbox = pygame.draw.rect(win, white, (self.x, self.y, 29, 70))
    if hitbox.colliderect(enemy):
        print("HIT")


class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 3 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def draw_frame():
    win.fill(white)
    draw_2(player1, win)
    draw_2(player2, win)
    for special in special_move_1:
        special.draw(win)

    pygame.display.update()


def player1_movement(self):
    check_collide(self, player2)
    # for loop for special attack
    for special in special_move_1:
        if screen_width > special.x > 0:
            special.x += special.vel
        else:
            special_move_1.pop(special_move_1.index(special))
    fps_clock.tick(fps)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        # add parameter that stores charge-up, add if that checks if charge-up is at desired value and execute, else print "NEED MORE ENERGY"
        if self.left:
            facing = -1
        else:
            facing = 1
        if len(special_move_1) < 1:
            special_move_1.append(
                Projectile(round(self.x + self.width // 2), round(self.y + self.height // 2),
                           radius=6, color=blue, facing=facing))
    # moving left
    if keys[pygame.K_a] and self.x > self.vel:
        self.x -= self.vel
        self.left = True
        self.right = False
        self.standing = False
    # moving right
    elif keys[pygame.K_d] and self.x < screen_width - self.width - self.vel:
        self.x += self.vel
        self.left = False
        self.right = True
        self.standing = False
    # standing still
    else:
        self.standing = True
        self.walk_count = 0
    # jumping, checks if we are not jumping and if we are not we can jump
    if not self.is_jump:
        if keys[pygame.K_SPACE]:
            self.is_jump = True
            self.left = False
            self.right = False
            self.walk_count = 0
    else:
        if self.jump_count >= -10:
            neg_1 = 1
            if self.jump_count < 0:
                neg_1 = -1
            # hastigeten på hoppet, höjd på hoppet,
            self.y -= (self.jump_count ** 2) * 0.5 * neg_1
            self.jump_count -= 1
        else:
            self.is_jump = False
            self.jump_count = 10


def player2_movement(self):
    check_collide(self, player1)
    # for loop for special attack
    for special in special_move_2:
        if screen_width > special.x > 0:
            special.x += special.vel
        else:
            special_move_2.pop(special_move_2.index(special))
    fps_clock.tick(fps)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_u]:
        # add parameter that stores charge-up, add if that checks if charge-up is at desired value and execute, else print "NEED MORE ENERGY"
        if self.left:
            facing = -1
        else:
            facing = 1
        if len(special_move_2) < 1:
            special_move_2.append(
                Projectile(round(self.x + self.width // 2), round(self.y + self.height // 2),
                           radius=6, color=blue, facing=facing))
    # moving left
    if keys[pygame.K_LEFT] and self.x > self.vel:
        self.x -= self.vel
        self.left = True
        self.right = False
        self.standing = False
    # moving right
    elif keys[pygame.K_RIGHT] and self.x < screen_width - self.width - self.vel:
        self.x += self.vel
        self.left = False
        self.right = True
        self.standing = False
    # standing still
    else:
        self.standing = True
        self.walk_count = 0
    # jumping, checks if we are not jumping and if we are not we can jump
    if not self.is_jump:
        if keys[pygame.K_j]:
            self.is_jump = True
            self.left = False
            self.right = False
            self.walk_count = 0
    else:
        if self.jump_count >= -10:
            neg = 1
            if self.jump_count < 0:
                neg = -1
            self.y -= (self.jump_count ** 2) * 0.5 * neg
            self.jump_count -= 1
        else:
            self.is_jump = False
            self.jump_count = 10


# mainloop
special_move_1 = []
special_move_2 = []
player1 = Player(300, 500, 40, 70)
player2 = Player(800, 500, 40, 70)
running = True

while running:
    win.blit(casino_bg, (0, 0))
    pygame.display.update()
    # for loop for exiting the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player1_movement(player1)
    player2_movement(player2)
    draw_frame()

pygame.quit()
