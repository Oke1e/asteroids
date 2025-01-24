import pygame
from constants import *
from player import Player

def main():
    #Setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game Loop
    try:
        while True:
            dt = clock.tick(60) / 1000

            #Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            player.update(dt)

            #Draw
            screen.fill((0, 0, 0))
            player.draw(screen)
            pygame.display.flip()
    
    except KeyboardInterrupt:
        print("\nExiting game loop. Goodbye!")



if __name__ == "__main__":
    main()
