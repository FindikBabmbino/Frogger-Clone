import pygame

class SimpleSprite(pygame.sprite.Sprite):
	def __init__(self,surf,pos,groups):
		super().__init__(groups)
		self.image=surf
		self.rect=self.image.get_rect(topleft=pos)
		self.hitbox=self.rect.inflate(0,-self.rect.height/2)