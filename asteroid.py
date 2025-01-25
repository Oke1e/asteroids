import pygame
import random
from pygame.math import Vector2
from constants import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size=ASTEROID_LARGE):
        pygame.sprite.Sprite.__init__(self, *self.containers)
        self.position = self._get_spawn_position()
        self.rotation = random.uniform(0, 360)
        self.radius = random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MIN_RADIUS * 2)
        surface_multiplier = 6  # Increased from 4 to 6
        surface_size = self.radius * surface_multiplier
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)
        direction = Vector2(1,0).rotate(random.uniform(0,360))
        self.velocity = direction * ASTEROID_SPEED
        self.rotation_speed = ASTEROID_ROTATION_SPEED * random.choice([-1,1])
        self.vertices = self._generate_vertices()
        if size == ASTEROID_SMALL:
            self.radius = ASTEROID_SMALL
        elif size == ASTEROID_MEDIUM:
            self.radius = ASTEROID_MEDIUM
        else:
            self.radius = ASTEROID_LARGE



    def _generate_vertices(self):
        vertices = []
        center = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2)
        
        for i in range(ASTEROID_VERTICES):
            angle = i * (360 / ASTEROID_VERTICES)
            # Vary the radius randomly
            rand_radius = self.radius * (1 - ASTEROID_IRREGULARITY + random.random() * ASTEROID_IRREGULARITY)
            # Convert angle to radians and calculate position
            vertex = center + pygame.Vector2(0, rand_radius).rotate(-angle)
            vertices.append(vertex)
        return vertices


    def _get_spawn_position(self):

     
        # First, choose a random edge (0: top, 1: right, 2: bottom, 3: left)
        edge = random.randint(0, 3)
        
        if edge == 0:  # Top edge
            return Vector2(
                random.randint(0, SCREEN_WIDTH),
                -ASTEROID_MIN_RADIUS
            )
        elif edge == 1:  # Right edge
            return Vector2(
                SCREEN_WIDTH + ASTEROID_MIN_RADIUS,
                random.randint(0, SCREEN_HEIGHT)
            )
        elif edge == 2:  # Bottom edge
            return Vector2(
                random.randint(0, SCREEN_WIDTH),
                SCREEN_HEIGHT + ASTEROID_MIN_RADIUS
            )
        else:  # Left edge
            return Vector2(
                -ASTEROID_MIN_RADIUS,
                random.randint(0, SCREEN_HEIGHT)
            )
        
    def update(self, dt):
        self.rotation += self.rotation_speed * dt
        self.position += self.velocity * dt
        
        # Wrap around screen edges
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

        # Clear current surface
        self.image.fill((0, 0, 0, 0))
        
        # Get rotated vertices
        rotated_vertices = []
        center = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2)
        for vertex in self.vertices:
            # Translate to origin, rotate, translate back
            offset = vertex - center
            rotated = offset.rotate(self.rotation)
            rotated_vertices.append(rotated + center)
        
        # Draw the asteroid
        pygame.draw.polygon(self.image, "white", rotated_vertices, 2)
        
        # Update rect position
        self.rect.center = self.position

    def triangle(self):
        # Reuse your triangle vertices code here
        center = pygame.Vector2(self.radius * 1.5, self.radius * 1.5)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 2
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
        