import pygame
from pygame.math import Vector2


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # We will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub-classes must override
        pass

    def update(self, dt):
        # Sub-classes must override
        pass
    
    def check_collision(self, other_circle):
        distance_to = self.position.distance_to(other_circle.position)
        
        if distance_to <= self.radius + other_circle.radius:
            return True
        else:
            return False
        


