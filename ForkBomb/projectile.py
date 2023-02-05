import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, facing_right):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("images/projectile.png")

        if facing_right == True:
            self.image = image
            pos_y -= 7
            pos_x += 25
            self.rect = self.image.get_rect(center=(pos_x, pos_y))
            self.direction = 10
        else:
            pos_y -= 7
            pos_x -= 25
            self.image = pygame.transform.flip(image, True, False)
            self.rect = self.image.get_rect(center=(pos_x, pos_y))
            self.direction = -10

    def update(self, shift):
        self.rect.x += shift
        self.rect.x += self.direction
