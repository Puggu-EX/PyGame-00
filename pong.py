import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,  720))

"""
Game Variables
"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(144)