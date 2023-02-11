import pygame, sys, settings 
from pygame.locals import *
input_rect = pygame.Rect(200,200,140,32)
color = pygame.Color("lightskyblue3")

class console_input():
    def __init__(self, screen):
        print(str(settings.active))
        
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
        console_input.start(self)
    
    def start(self):
        pg = pygame
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        settings.active = not settings.active
                    else:
                        settings.active = False
                if event.type == pygame.KEYDOWN:
                    if settings.active:
                        print("Active")
                        if event.key == pygame.K_RETURN:
                            print(settings.userText)
                            settings.userText = ''
                        elif event.key == pygame.K_BACKSPACE:
                            settings.userText = settings.userText[:-1]
                        else:
                            settings.userText += event.unicode
        
        self.color = self.color_active if settings.active else self.color_passive
        txt_surface = settings.font.render(settings.userText, True, self.color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        self.input_box.w = width
        self.screen.fill("grey", self.input_box)
        # Blit the text.
        self.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        
        txt_surface = settings.font.render("Press F1 For Stats!", True, self.color)
        self.screen.blit(txt_surface, ((0,50)))
        # Blit the input_box rect.
        pg.draw.rect(self.screen, color, self.input_box, 2)
        
        
