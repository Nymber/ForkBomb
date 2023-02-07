import threading
import pygame
import sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
background = pygame.image.load("images/background.png")
clock = pygame.time.Clock()
lock = threading.Lock()
level = Level(level_map, screen, lock)
game = threading.Thread(target = level.run(), name='game', args=(),kwargs={})

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # set background color to our window
    screen.blit(background, (0, 0))
    game.start()

    # Update our window
    pygame.display.update()
    clock.tick(60)

