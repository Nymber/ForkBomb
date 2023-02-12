import pygame, settings
from pygame.locals import *

#initialize
class consoleSystem():
    def __init__(self, screen, status = 1):
        self.screen = screen
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.color = self.color_passive
        self.Data = list()
        self.Data = [settings.username, settings.password, settings.money, settings.power, settings.power, settings.memory, settings.connection, settings.power, settings.bitcoin]
        self.timeout = 0
        self.input_box = pygame.Rect(30, 100, 40, 32)
        self.color_passive = pygame.Color('blue')
        self.color_active = pygame.Color('black')
        self.surface_text = settings.font.render(str(self.Data), True, "blue")
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
        
        settings.screen.blit(self.throw, settings.Data_center)
        
        
        self.status = 0
        
    def update(self):
        if(self.status == True):
            self.throw = settings.font.render(str(self.Data), 30, True, (255,255,255))
