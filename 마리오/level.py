import pygame
from settings import tile_size, screen_width
from tiles import Tile
from player import Player

class Level:
    def __init__(self, level_data, surface):
        super().__init__()
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, level_data):
        self.tiles = pygame.sprite.Group()              # a container class to hold and manage multiple sprite objects
                                                        # there are tiles
        self.player = pygame.sprite.GroupSingle()       # group container that holds a single sprite
                                                        # there is just one player

        for row_index, row in enumerate(level_data):
            for col_index, cell in enumerate(row):

                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile(tile_size, (x, y))
                    self.tiles.add(tile)        # add sprites to this group

                elif cell == 'P':
                    player = Player((x, y))
                    self.player.add(player)     # add a single sprite to this group

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            # when player moves to the left
            # if player moves too far from the right
            # then camera moves to the left by moving the entire map to the right
            self.world_shift = 8
            player.player_speed = 2

        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            # when player moves to the right
            # if player moves too far from the left
            # then camera moves to the right by moving the entire map to the left
            self.world_shift = -8
            player.player_speed = 0

        else:
            self.world_shift = 0
            player.player_speed = 8

    # check horizontal collision and vertical collision each other
    # to access to the rectangle of each of the tile
    # using rect.colliderect is better than sprite.collide_rect (more convenient)
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.player_speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)