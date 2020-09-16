import pygame, sys


# This is my first project using python and Pygame. Hoping to create various simple games.
# Including but not limited to: Snake Game, Space Invaders, Pong, Super Mario, and Tron.

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    # screen.blit(floor_surface, (floor_x_pos + 576//2, 400))



pygame.init()
screen = pygame.display.set_mode((576 // 2, 1024 // 2))
clock = pygame.time.Clock()

floor_x_pos = 0

bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(576,115))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))

    draw_floor()
    floor_x_pos -= 1
    if floor_x_pos == -576//2:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(144)
