import pygame, sys, settings 
from pygame.locals import *
pygame.init()
input_rect = pygame.Rect(200,200,140,32)
color = pygame.Color("lightskyblue3")

class console_input:
    def __init__(self, Data):
        self.Data = Data
        self.active = False
        self.color_passive = pygame.Color('chartreuse4')
        self.color_active = pygame.Color('lightskyblue3')
        self.surface_text = settings.font.render(str(self.Data), True, "blue")
        console_input.start(self)
    
    def start(self):
        pygame.init()
        for event in pygame.event.get(self.active, Color):    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textRect2.collidepoint(event.pos):
                    
                    self.active = True
                else:
                    self.active = False 
            if event.type == KEYDOWN:
                if event.type == pygame.K_BACKSPACE:
                    settings.userText = settings.userText[0:-1]
                else:
                    settings.userText += event.unicode 
                    throw1 = settings.font.render(str(settings.msg), True, "blue")
                    settings.screen.blit(throw1, (0, 30))
                    textRect1 = throw1.get_rect()
                    settings.screen.blit(self.surface_text, (0, 50))
                    textRect2 = self.surface_text.get_rect()
            if self.active:
                color = self.color_active
            else:
                color = self.color_passive
            settings.screen.blit(self.surface_text,(0,50))
            
        
    