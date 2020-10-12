import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

fps_clock = pygame.time.Clock()
fps = 60

box = pygame.Rect(400, 300, 50, 30)
vel = 5


running = True
while running:
    fps_clock.tick(fps)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_a] and box.x > 0:
            box.x -= vel

        if keys[pygame.K_d] and box.x < screen_width-50:
            box.x += vel

    screen.fill((255, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), box)
    pygame.display.update()