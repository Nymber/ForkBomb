import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, size, code):
        super().__init__()

        if code == "tile":
            self.image = pygame.image.load(
                "images/tile.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        if code == "wall":
            self.image = pygame.image.load(
                "images/end.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
