
import  pygame, consoleInput
from consoleInput import console_input
from settings import *
import settings
from login import Login
from level import Level

# Pygame setup
pygame.init()
background = pygame.image.load("images/background.png")
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
class startGame():
    def start(lock):
        infoGrab = False
        level = Level(level_map, screen)
        login = Login(screen)
        while True:
            lock.acquire()
            
            screen.blit(background, (0, 0))
            
            if(infoGrab == True):
                consoleInput.console_input(screen)
                level.run()
            else: 
                infoGrab = login.run()
                
            pygame.display.update()
            dt = clock.tick(60)
            lock.release()