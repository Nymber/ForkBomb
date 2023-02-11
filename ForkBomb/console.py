import pygame
import time
import settings
from pygame.locals import *

#initialize
pygame.init()

class consoleSystem():
    def __init__(self, status):
        self.Data = list()
        self.Data = [settings.username, settings.password, settings.money, settings.power, settings.power, settings.memory, settings.connection, settings.power, settings.bitcoin]
        self.status = status
        self.keys = pygame.key.get_pressed()
        consoleSystem.start(self)
        
    def message_to_display(self):
        throw = settings.font.render(str(self.Data), True, "blue")
        settings.screen.blit(throw, (0, 30))
        
    def start(self):
        consoleSystem.update(self)
        print("Console Toggled!")
        
        settings.screen.blit(self.throw, settings.Data_center)
        
        
        self.status = 0
        
    def update(self):
        if(self.status == True):
            self.throw = settings.font.render(str(self.Data), 30, True, (255,255,255))
