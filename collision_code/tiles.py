import pygame 
from settings import * 

class Wall(pygame.sprite.Sprite):
	def __init__(self,x,y,*groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/rock.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = (x,y))