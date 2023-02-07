import threading
import pygame
import sys
from settings import *
from level import Level
from interface import startGame

# Pygame setup
pygame.init()
background = pygame.image.load("images/background.png")
clock = pygame.time.Clock()
lock = threading.Lock()

game = threading.Thread(target = startGame.start(lock), name='game', args=(),kwargs={})
game.start()

