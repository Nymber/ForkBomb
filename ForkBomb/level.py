import pygame
from tiles import Tile
from settings import tile_size, WIDTH
from player import Player
from enemy import Enemy
from projectile import Projectile


class Level:

    # default function when Level is instansialized
    def __init__(self, level_data, surface):
        self.previous_time = pygame.time.get_ticks()
        self.damage_time = pygame.time.get_ticks()
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.health = 3

    # sets position of tiles as well as the player
    def setup_level(self, layout):

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    code = "tile"
                    tile = Tile((x, y), tile_size, code)
                    self.tiles.add(tile)
                if cell == "W":
                    code = "wall"
                    tile = Tile((x, y), tile_size, code)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "E":
                    enemy_sprite = Enemy((x, y))
                    self.enemy_group.add(enemy_sprite)

    # camera scroll
    def scroll_x(self):

        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WIDTH - WIDTH + 150 and direction_x < 0:
            self.world_shift = 6
            player.speed = 0

        elif player_x > WIDTH - 150 and direction_x > 0:
            self.world_shift = -6
            player.speed = 0

        else:
            self.world_shift = 0
            player.speed = 6

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        enemy = self.enemy_group
        bullet = self.bullet_group

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

        for sprite in bullet:
            pygame.sprite.spritecollide(sprite, enemy, True)

        for sprite in enemy:
            if sprite.rect.colliderect(player.rect):
                self.current_time = pygame.time.get_ticks()
                if self.current_time - self.damage_time > 1000:
                    self.damage_time = self.current_time
                    self.health -= 1
                    if self.health < 1:
                        pygame.quit()
                    print(self.health)

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def iceBall(self):
        keys = pygame.key.get_pressed()
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery

        if keys[pygame.K_RIGHT]:
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.facing_right = False

        if keys[pygame.K_SPACE]:
            self.current_time = pygame.time.get_ticks()
            try:
                if self.current_time - self.previous_time > 500:
                    bullet = Projectile(player_x, player_y, self.facing_right)
                    self.bullet_group.add(bullet)
                    self.previous_time = self.current_time
            except:
                print("Must move first")

    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        # enemy
        self.enemy_group.draw(self.display_surface)
        self.enemy_group.update(self.world_shift)

        # projectile
        self.iceBall()
        self.bullet_group.draw(self.display_surface)
        self.bullet_group.update(self.world_shift)
