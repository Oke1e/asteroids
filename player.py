import pygame
from constants import *
from CircleShape import CircleShape
from pygame.math import Vector2
from bullet import Bullet


class Player(CircleShape, pygame.sprite.Sprite):
	def __init__(self,x, y):
		pygame.sprite.Sprite.__init__(self, *self.containers)
		CircleShape.__init__(self, x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_cooldown = 0
	
		self.image = pygame.Surface((PLAYER_RADIUS * 3, PLAYER_RADIUS * 3), pygame.SRCALPHA)
		self.rect = self.image.get_rect(center = (x, y))
	
	def triangle(self):
		center = pygame.Vector2(PLAYER_RADIUS * 1.5, PLAYER_RADIUS * 1.5)
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 2
		a = center + forward * self.radius
		b = center - forward * self.radius - right
		c = center - forward * self.radius + right
		return [a, b, c]


	def rotate(self, dt):
		self.rotation += dt

	def update(self, dt):
		
		if self.shoot_cooldown > 0:
			self.shoot_cooldown -= dt

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(PLAYER_TURN_SPEED * -dt)
		if keys[pygame.K_d]:
			self.rotate(PLAYER_TURN_SPEED * dt)
		if keys[pygame.K_w]:
			self.move(dt)	
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
			self.shoot()
			self.shoot_cooldown = .25
			#def draw(self, screen):
		self.image.fill((0, 0, 0, 0))
		pygame.draw.polygon(self.image, "white", self.triangle(), 2)

	def shoot(self):
		# Create a bullet at the player's position, moving in the direction they're facing
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		bullet_pos = self.position + forward * self.radius
		Bullet(bullet_pos, forward)	

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
		self.rect.center = self.position
		print(f"Position: {self.position}, Rect Center: {self.rect.center}, Image size: {self.image.get_size()}")
		#print(f"Position after: {self.position}")
		#reverse = pygame.Vector2(0, -1).rotate(self.rotation)
		#self.position += reverse * dt



		
