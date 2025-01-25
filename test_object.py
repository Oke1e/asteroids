import pygame
from constants import *

class TestObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(*self.containers)
        print("Creating TestObject")
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = ASTEROID_MIN_RADIUS
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(center = self.position)
        self.image.fill("red")

    def rotate(self, angle):
        self.rotation = (self.rotation + angle) % 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * ASTEROID_SPEED * dt
        self.rect.center = self.position

    def triangle(self):
        # Similar to Player's triangle but maybe a different shape?
        center = pygame.Vector2(self.radius * 1.5, self.radius * 1.5)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        print("Updating TestObject")
        self.rotate(ASTEROID_TURN_SPEED * dt)
        # Clear the surface
        self.image.fill((0, 0, 0, 0))
        # Draw the new triangle
        pygame.draw.polygon(self.image, "red", self.triangle(), 2)
        # Update rect position
        self.rect.center = self.position