#pip install pygame

import math
import random
import time
import pygame

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Aim Trainer")

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pyge.QUIT:
                run = False
                break