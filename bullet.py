import pygame
from pygame.math import Vector2
from constants import BULLET_SPEED, BULLET_LIFETIME, BULLET_SIZE

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        pygame.sprite.Sprite.__init__(self, *self.containers)
        self.position = Vector2(position)
        self.velocity = direction * BULLET_SPEED
        self.lifetime = BULLET_LIFETIME
        self.radius = BULLET_SIZE
        
        # Create the bullet's image
        self.image = pygame.Surface((BULLET_SIZE * 2, BULLET_SIZE * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (BULLET_SIZE, BULLET_SIZE), BULLET_SIZE)
        self.rect = self.image.get_rect(center=self.position)
        
    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()  # Remove bullet when lifetime expires
            
        self.position += self.velocity * dt
        self.rect.center = self.position