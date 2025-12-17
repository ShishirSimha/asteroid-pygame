import pygame
import constants
from logger import log_state

pygame.init()

def main():
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT));

    #game loop
    while True:
        log_state()

        #check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fill the screen canvas with black as background colour
        screen.fill("black")

        pygame.display.flip()


if __name__ == "__main__":
    main()
