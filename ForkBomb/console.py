import pygame
import time
from settings import *
from pygame.locals import *

#initialize
pygame.init()

class consoleSystem:
    def __init__(self,msg,font,screen):
        print("Console Toggled!")
        self.msg = msg
        self.font = font
        self.screen = screen
        sysLog = open("gameConsoleLog.txt","r")
        __msg = sysLog.readlines()
        print(__msg)
        if(msg != __msg):
            msg = __msg
            pygame.font.init()
            throw = font.render(str(msg), 30, True, "blue")
            textRect = throw.get_rect()
            textRect.center = (500, 800)
            screen.blit(throw, textRect)
            pygame.display.update()
        else:
            print("same stats")
            return self.msg
    def message_to_display(self, font, msg):
        throw = font.render(str(msg), True, "blue")
        screen.blit(throw, (0, 0))
    



