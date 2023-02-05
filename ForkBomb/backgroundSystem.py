import pygame
import sys
import settings

class player():
    #Inject data
    def inject():
        sysLog = open("gameConsoleLog.txt","w")
        sysLog.writelines(str(settings.Data))
    #Inject data