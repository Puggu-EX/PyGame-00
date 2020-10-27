import sys
import pygame
from random import randint


def draw_brick(bricks):
    count = 0
    for brick in bricks:
        if 0 <= count <= 11:
            screen.blit(brick_surface_teel, brick)
        elif 12 <= count <= 23:
            screen.blit(brick_surface_purple, brick)
        elif 24 <= count <= 35:
            screen.blit(brick_surface_blue, brick)
        elif 36 <= count <= 47:
            screen.blit(brick_surface_cyan, brick)
        elif 48 <= count <= 69:
            screen.blit(brick_surface_green, brick)
        count += 1


def delete_brick():
    pass

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))

"""
Game Variables
"""
# Brick Surface
brick_surface_blue_01 = pygame.image.load('assets/brick_breaker_assets/01-Breakout-Tiles.png')
brick_surface_blue_02 = pygame.image.load('assets/brick_breaker_assets/02-Breakout-Tiles.png')
brick_surface_blue = brick_surface_blue_01
brick_surface_blue = pygame.transform.scale(brick_surface_blue, (85, 35))

brick_surface_teel_01 = pygame.image.load('assets/brick_breaker_assets/17-Breakout-Tiles.png')
brick_surface_teel_02 = pygame.image.load('assets/brick_breaker_assets/18-Breakout-Tiles.png')
brick_surface_teel = brick_surface_teel_01
brick_surface_teel = pygame.transform.scale(brick_surface_teel, (85, 35))

brick_surface_green_01 = pygame.image.load('assets/brick_breaker_assets/03-Breakout-Tiles.png')
brick_surface_green_02 = pygame.image.load('assets/brick_breaker_assets/04-Breakout-Tiles.png')
brick_surface_green = brick_surface_green_01
brick_surface_green = pygame.transform.scale(brick_surface_green, (85, 35))

brick_surface_purple_01 = pygame.image.load('assets/brick_breaker_assets/05-Breakout-Tiles.png')
brick_surface_purple_02 = pygame.image.load('assets/brick_breaker_assets/06-Breakout-Tiles.png')
brick_surface_purple = brick_surface_purple_01
brick_surface_purple = pygame.transform.scale(brick_surface_purple, (85, 35))

brick_surface_cyan_01 = pygame.image.load('assets/brick_breaker_assets/11-Breakout-Tiles.png')
brick_surface_cyan_02 = pygame.image.load('assets/brick_breaker_assets/12-Breakout-Tiles.png')
brick_surface_cyan = brick_surface_cyan_01
brick_surface_cyan = pygame.transform.scale(brick_surface_cyan, (85, 35))

background_surface = pygame.image.load('assets/background-night.png')
background_surface = pygame.transform.scale(background_surface, (1280, 720))

CREATEBRICK = pygame.USEREVENT
pygame.time.set_timer(CREATEBRICK, 1000)

brick_list = []
brick_list.clear()
count_x = 45
count_y = 10
for i in range(5):
    if i != 0:
        count_y += 50
    for j in range(12):
        new_brick = brick_surface_teel.get_rect(topleft=(count_x, count_y))
        count_x += 100
        if count_x == 1245:
            count_x = 45
        brick_list.append(new_brick)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CREATEBRICK:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = randint(0, 10)

    screen.blit(background_surface, (0, 0))
    draw_brick(brick_list)

    pygame.display.update()
    clock.tick(144)
