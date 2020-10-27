import pygame

brick_list = []

class Brick(object):
    def __init__(self, brick_h, brick_w):
        current_surface = pygame.image.load("assets/brick_breaker_assets/0{}-Breakout-Tiles.png".format(1))
        current_surface = pygame.transform.scale(current_surface, (brick_w, brick_h))
        brick_list.append(current_surface)
        brick_w = 85
        brick_h = 35