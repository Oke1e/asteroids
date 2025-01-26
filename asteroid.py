import pygame
import random
from pygame.math import Vector2
from constants import *
from CircleShape import *

pygame.font.init()
FONT = pygame.font.Font(None, 24)

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, size=ASTEROID_LARGE):
        print(f"Creating new asteroid with size parameter: {size}")
        print(f"ASTEROID_LARGE = {ASTEROID_LARGE}")
        
        self.position = self._get_spawn_position()

        if size == ASTEROID_SMALL:
            self.radius = ASTEROID_SMALL
        elif size == ASTEROID_MEDIUM:
            self.radius = ASTEROID_MEDIUM
        else:
            self.radius = ASTEROID_LARGE

        CircleShape.__init__(self, self.position.x, self.position.y, size)
        pygame.sprite.Sprite.__init__(self, *self.containers)
        
        self.rotation = random.uniform(0, 360)
        surface_multiplier = 6  # Increased from 4 to 6
        surface_size = self.radius * surface_multiplier
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)
        direction = Vector2(1,0).rotate(random.uniform(0,360))
        self.velocity = direction * ASTEROID_SPEED
        self.rotation_speed = ASTEROID_ROTATION_SPEED * random.choice([-1,1])
        self.vertices = self._generate_vertices()
       



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

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)
    
    # Add label
        size_text = "Large" if self.radius == ASTEROID_LARGE else "Medium" if self.radius == ASTEROID_MEDIUM else "Small"
        text_surface = FONT.render(f"{size_text} ({self.radius})", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.position.x, self.position.y - self.radius - 10))
        surface.blit(text_surface, text_rect)

    def triangle(self):
        # Reuse your triangle vertices code here
        center = pygame.Vector2(self.radius * 1.5, self.radius * 1.5)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 2
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    
    def split(self):
        print("=== Asteroid Debug ===")
        print(f"Asteroid radius: {self.radius}")
        print(f"Is radius <= ASTEROID_MIN_RADIUS? {self.radius <= ASTEROID_MIN_RADIUS}")
        print(f"Is radius == ASTEROID_LARGE? {self.radius == ASTEROID_LARGE}")
        print(f"Is radius == ASTEROID_MEDIUM? {self.radius == ASTEROID_MEDIUM}")
        print(f"Type of self.radius: {type(self.radius)}")
        print(f"Type of ASTEROID_MEDIUM: {type(ASTEROID_MEDIUM)}")
        print("====================")
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        self.kill()

        current_pos = Vector2(self.position)
        current_vel = Vector2(self.velocity)
        current_radius = self.radius

        
        
        new_size = None
        if current_radius == ASTEROID_LARGE:
            new_size = ASTEROID_MEDIUM
        elif current_radius == ASTEROID_MEDIUM:
            new_size = ASTEROID_SMALL
        else:
            self.kill()
            return
        
        self.kill()
        
        random_angle = random.uniform(20,50)
        new_vector1 = self.velocity.rotate(random_angle) * 1.2
        new_vector2 = self.velocity.rotate(-random_angle) * 1.2

        new_asteroid1 = Asteroid(new_size)
        new_asteroid2 = Asteroid(new_size)

        new_asteroid1.position = Vector2(self.position)
        new_asteroid2.position = Vector2(self.position)
        new_asteroid1.velocity = new_vector1
        new_asteroid2.velocity = new_vector2



        
        