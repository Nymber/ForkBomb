from ctypes.wintypes import MSG
from pickle import TRUE
import pygame
import time
import settings
from settings import *
from pygame.locals import *


#initialize
pygame.init()
#initialize

class consoleSystem:
    global msg
    msg = " "
    def statMsg():
        global msg
        sysLog = open("gameConsoleLog.txt","r")
        __msg = sysLog.readlines()
        print(__msg)
        if(msg != __msg):
            msg = __msg
            __throw = consoleSystem.fontMethod(msg)
            screen.blit(__throw, (0, 0))

            return __throw
        else:
            print("same stats")
            return msg
                

    def fontMethod(msg):
        pygame.font.init()
        throw = font.render(str(msg), True, pygame.Color("chartreuse"), pygame.Color("firebrick"))
        return throw

    def toggleConsole(bol):
        keys = pygame.key.get_pressed()
        print("console toggled")
        while bol >= 1:
            time.sleep(.6)
            consoleSystem.statMsg()
            if keys[pygame.K_F1]:
                bol = 0
                pygame.font.quit()

    def message_to_display(msg ,color):
        msg = ""
        throw = font.render(str(msg), True, color)
        screen.blit(throw, (0, 0))



