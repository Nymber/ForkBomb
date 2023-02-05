import pygame
from settings import WIDTH
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("images/enemy/enemy.png")
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

        # enemy movement
        self.direction = -1
        self.speed = 3
        self.gravity = 0.8
        self.jump_speed = -16
        self.move_counter = 0

    def movement(self):
        self.rect.x += self.direction * self.speed
        self.move_counter += 1
        if self.move_counter > 40:
            self.direction *= -1
            flipped_image = pygame.transform.flip(self.image, True, False)
            self.image = flipped_image
            self.move_counter = 0

    def update(self, shift):
        self.rect.x += shift
        self.movement()
