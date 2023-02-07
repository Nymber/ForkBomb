import level
import threading
import threading
import pygame
import sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
background = pygame.image.load("images/background.png")
clock = pygame.time.Clock()

class startGame():
    def start(lock):
        level = Level(level_map, screen)
        while True:
            lock.acquire()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # set background color to our window
            screen.blit(background, (0, 0))
            level.run()

            # Update our window
            pygame.display.update()
            clock.tick(60)
            lock.release()
            

            