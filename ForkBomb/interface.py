
import threading, pygame, console, consoleInput, sys
from consoleInput import console_input
from settings import *
import settings
from level import Level

# Pygame setup
pygame.init()
background = pygame.image.load("images/background.png")
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
class startGame():
    def start(lock):
        level = Level(level_map, screen)
        
        while True:
            lock.acquire()
            
            screen.blit(background, (0, 0))
            
            consoleInput.console_input(screen)
            level.run()
            
            pygame.display.update()
            dt = clock.tick(60)
            lock.release()