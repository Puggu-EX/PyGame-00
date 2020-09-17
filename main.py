import pygame, sys


# This is my first project using python and Pygame. Hoping to create various simple games.
# Including but not limited to: Snake Game, Space Invaders, Pong, Super Mario, and Tron.

def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop=(screen_w // 4, screen_h // 4))
    return new_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    # screen.blit(floor_surface, (floor_x_pos + 576//2, 400))


screen_w = 576
screen_h = 1024

pygame.init()
screen = pygame.display.set_mode((screen_w // 2, screen_h // 2))
clock = pygame.time.Clock()

# Game Variables
gravity = .25
bird_movement = 0.0

bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (576, 115))
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
# bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=((screen_w // 4) - 100, screen_h // 4))

pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0.0
                bird_movement -= 6.0
            elif event.key == pygame.K_BACKSPACE:
                pygame.quit()
                sys.exit()
        if event.type == SPAWNPIPE:
            print("Pipe Spawn")
            pipe_list.append(create_pipe())

    # Bird Movement
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # Draws surfaces
    screen.blit(bg_surface, (0, 0))
    screen.blit(bird_surface, bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    draw_floor()
    floor_x_pos -= 1
    if floor_x_pos == -576 // 2:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
