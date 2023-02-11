#imports
import pygame
#imports


#map settings
level_map = [
    ' WW         E                  E     XXX          E           WW ',
    ' WW         E           XXX       E     XXX          E           WW ',
    ' WW         E   XXX               E     XXX          E           WW ',
    ' WW      XXX   E              XXX    E           XXX    E           WW ',
    ' WW         E   XXX               E     XXX          E           WW ',
    ' WW       XXX          XXX          XXX  E             E     E   WW ',
    ' WW                        XXX             XXX             XXX   WW ',
    ' WW P           E                                          XXX   WW ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX   XX  XXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 50
clock = pygame.time.Clock()
WIDTH = 1200
HEIGHT = len(level_map) * tile_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#map settings

pygame.font.init()


#program clientUserSettings
username = "test"
password = "test"
money = 0
power = 1
memory = 1 
connection = 1
bitcoin = 0
#program clientUserSettings

msg = " "
userText = ""
#dataToSaveFile 
Data_center = (150, 5)
#dataToSaveFile


#fontValues
font = pygame.font.SysFont("Verdana", 12)
#fontValues