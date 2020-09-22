import random
import sys
from time import sleep

import pygame


# This is my first project using python and Pygame. Flappy Birds :D

def create_pipe():
    # random_pipe_pos = random.choice(pipe_height)
    # new_pipe_top = pipe_surface.get_rect(midbottom=((screen_w // 2) + 50, random_pipe_pos - 140))
    # new_pipe = pipe_surface.get_rect(midtop=((screen_w // 2) + 50, random_pipe_pos))

    x = random.randint(200, 350)
    new_pipe_top = pipe_surface.get_rect(midbottom=((screen_w // 2) + 50, x - 140))
    new_pipe = pipe_surface.get_rect(midtop=((screen_w // 2) + 50, x))
    return new_pipe, new_pipe_top


def slow_print(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.1)
    print("")


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024 // 2:
            screen.blit(pipe_surface, pipe)
        else:
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50:
        return False
    elif bird_rect.bottom >= 400:
        return False
    return True


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    # screen.blit(floor_surface, (floor_x_pos + 576//2, 400))


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 8, 1)
    return new_bird


screen_w = 576
screen_h = 1024

pygame.init()
screen = pygame.display.set_mode((screen_w // 2, screen_h // 2))
clock = pygame.time.Clock()

###### Game Variables #######
gravity = .12
bird_movement = 0.0

game_active = True

# Background Surface
bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale2x(bg_surface)

# Floor Surface
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (576, 115))
floor_x_pos = 0

# Bird Surface

bird_downflap = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=((screen_w // 4) - 100, screen_h // 4))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)

# bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# bird_surface = pygame.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center=((screen_w // 4) - 100, screen_h // 4))

# Pipe Surface, List, Entity, Spawn Timer, Height List
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
flip_pipe = pygame.transform.flip(pipe_surface, False, True)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
# pipe_height = [200, 250, 300, 350]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Key Register Event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0.0
                bird_movement -= 4.0
            elif event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 250)
                bird_movement = -5
            elif event.key == pygame.K_BACKSPACE:
                pygame.quit()
                sys.exit()
        # Pipe spawn event
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            # print("Pipe Spawn: ", len(pipe_list))

            # De-spawn Pipes
            if len(pipe_list) > 6:
                pipe_list.pop(0)
                pipe_list.pop(1)
        if event.type == BIRDFLAP:
            if
            bird_index += 1

    # Draws surfaces
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        rotated_bird = rotate_bird(bird_surface)

        # Bird Movement
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)

        # Keep Game Active / Check Collision
        game_active = check_collision(pipe_list)

    # Floor
    draw_floor()
    floor_x_pos -= 1.5
    if floor_x_pos == -576 // 2:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(144)
