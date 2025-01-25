import pygame
from constants import *
from player import Player
from test_object import TestObject

def main():

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    TestObject.containers = (updatable, drawable)
    #Setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    test_obj1 = TestObject(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3)
    test_obj2 = TestObject(SCREEN_WIDTH * 2/3, SCREEN_HEIGHT * 2/3)
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
        
            #Draw
            screen.fill((0, 0, 0))
            #for sprite in drawable:
                #sprite.draw(screen)
            drawable.draw(screen)
            pygame.display.flip()
    
    except KeyboardInterrupt:
        print("\nExiting game loop. Goodbye!")



if __name__ == "__main__":
    main()
