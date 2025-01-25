import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from bullet import Bullet

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
            hits = pygame.sprite.groupcollide(bullet_group, asteroids_group, True, True, pygame.sprite.collide_circle)
            #Draw
            screen.fill((0, 0, 0))
            drawable.draw(screen)
            pygame.display.flip()
    
    except KeyboardInterrupt:
        print("\nExiting game loop. Goodbye!")



if __name__ == "__main__":
    main()
