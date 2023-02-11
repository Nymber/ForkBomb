
import threading, pygame, console, consoleInput, sys, level, backgroundSystem
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
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # set background color to our window
            screen.blit(background, (0, 0))
            level.run()
            
            settings.money = (settings.money + 10)
            print(settings.money)
            
            # Update our window
            pygame.display.update()
            clock.tick(60)
            
            lock.release()
            

            