import pygame, sys
from settings import *
from player import Player
from tiles import Wall
from debug import debug

class Level:
	def __init__(self):

		# general 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.all_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		
		# sprites
		self.world_setup()
		self.player = Player(200,100,self)

	def world_setup(self):
		for row_index, row in enumerate(world_map):
			for col_index, col in enumerate(row):
				if col == 'x':
					x = col_index * tile_size
					y = row_index * tile_size
					Wall(x,y,self.all_sprites,self.obstacle_sprites)

	def run(self):
		self.all_sprites.update()
		self.all_sprites.y_sorted_camera_draw(self.player) 

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2(0,0)

	def y_sorted_camera_draw(self,player):
		
		self.offset.x = player.rect.centerx - 340
		self.offset.y = player.rect.centery - 340

		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_rect  = sprite.rect.topleft - self.offset
			self.surface.blit(sprite.image, offset_rect)