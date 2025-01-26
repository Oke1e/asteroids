import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from bullet import Bullet
import sys
from CircleShape import *

pygame.font.init()
FONT = pygame.font.Font(None, 24)

def main():

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids_group)
    Bullet.containers = (updatable, drawable, bullet_group)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    #Setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Create game objects
    
    for _ in range(3):
        Asteroid(ASTEROID_LARGE)
    for _ in range(4):
        Asteroid(ASTEROID_MEDIUM)
    for _ in range(5):
        Asteroid(ASTEROID_SMALL)
    # After creating player and test objects
    print(f"Number of sprites in updatable: {len(updatable)}")
    print(f"Number of sprites in drawable: {len(drawable)}")
    print("Sprites in updatable:", [type(sprite).__name__ for sprite in updatable])
    print("Sprites in drawable:", [type(sprite).__name__ for sprite in drawable])

    #Game Loop
    try:
        while True:
            dt = clock.tick(60) / 1000

            #Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            updatable.update(dt)

            #for asteroid in asteroids_group:
                #if asteroid.check_collision(player):
                    #print("Game over!")
                    #sys.exit()
            
            for asteroid in asteroids_group:  # Iterate through all asteroid instances
                for bullet in bullet_group:  # Iterate through all bullet instances
                    if pygame.sprite.collide_circle(asteroid, bullet):  # For example, a circular collision check
                        bullet.kill()  # Remove the bullet from the game
                        asteroid.split()  # Split the asteroid

            #hits = pygame.sprite.groupcollide(bullet_group, asteroids_group, True, True, pygame.sprite.collide_circle)
            #Draw
            screen.fill((0, 0, 0))
            drawable.draw(screen)

            for asteroid in asteroids_group:
                size_text = "Large" if asteroid.radius == ASTEROID_LARGE else \
                            "Medium" if asteroid.radius == ASTEROID_MEDIUM else "Small"
                text_surface = FONT.render(f"{size_text} ({asteroid.radius})", True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(asteroid.position.x, asteroid.position.y - asteroid.radius - 10))
                screen.blit(text_surface, text_rect)
            pygame.display.flip()
    
    except KeyboardInterrupt:
        print("\nExiting game loop. Goodbye!")



if __name__ == "__main__":
    main()
