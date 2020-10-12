import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

walk_right = [pygame.image.load('pics//walking_right_2.png')]
walk_left = [pygame.image.load('pics//walking_left_1.png')]
char = [pygame.image.load('pics//look_left.png'), pygame.image.load('pics//look_right.png')]
fps_clock = pygame.time.Clock()
fps = 60




class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self, start_x, start_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        # Dessa x ocy y värdena bestämmer vart på skärmen gubben spawnar
        self.x = start_x
        self.y = start_y
        # width and height values that decide the size of the character
        self.width = width
        self.height = height
        # how many pixels the character is moving per action
        self.vel = 5
        # variables for the jumping mechanism
        self.is_jump = False
        self.jump_count = 10
        # counter for walking animation
        self.walk_count = 0
        # stating left and right
        self.left = False
        self.right = False
        self.standing = True
        self.rect = pygame.Rect(start_x, start_y, 29, 70)


def draw(self, screen):
    screen.fill(255, 255, 255)


player1 = Player(300, 150, 20, 20)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
