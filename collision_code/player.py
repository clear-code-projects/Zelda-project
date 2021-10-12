import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,x,y,game):
		
		# general
		super().__init__(game.all_sprites)
		self.image = pygame.image.load('graphics/player.png').convert_alpha()
		self.game = game
		
		# movement
		self.rect = self.image.get_rect(topleft = (x,y))
		self.direction = pygame.math.Vector2()
		self.speed = 6

		# collision
		self.hitbox = self.rect.copy().inflate(0,-26)

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

	def movement(self):

		# normalize vector
		if self.direction.magnitude() != 0: 
			self.direction = self.direction.normalize()
		
		# apply movement
		self.hitbox.x += self.direction.x * self.speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * self.speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.game.obstacle_sprites:
				if sprite.rect.colliderect(self.hitbox):
					if self.direction.x > 0: 
						self.hitbox.right = sprite.rect.left
					if self.direction.x < 0: 
		 				self.hitbox.left = sprite.rect.right
					self.direction.x = 0

		if direction == 'vertical':
			for sprite in self.game.obstacle_sprites:
				if sprite.rect.colliderect(self.hitbox):
					if self.direction.y > 0: 
						self.hitbox.bottom = sprite.rect.top
					if self.direction.y < 0: 
		 				self.hitbox.top = sprite.rect.bottom
					self.direction.y = 0

	def update(self):
		self.input()
		self.movement()
