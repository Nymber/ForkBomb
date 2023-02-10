from support import import_folder
from projectile import Projectile
import pygame
import console
import backgroundSystem
import consoleInput
class Player(pygame.sprite.Sprite):

    def __init__(self, pos, Data):
        
        super().__init__()
        self.Data = Data
        print("2: ",self.Data)
        self.previous_time = pygame.time.get_ticks()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = -16

        # player status
        self.status = 'idle'
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.facing_right = True
        
        

    def import_character_assets(self):
        character_path = 'images/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'attack': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):

        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        elif self.facing_right == False:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.jump()
        if keys[pygame.K_F1]:
            toggle = console.consoleSystem(True, self.Data)
        if keys[pygame.K_c]:
            consoleInput.console_input(self.Data)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'jump'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
