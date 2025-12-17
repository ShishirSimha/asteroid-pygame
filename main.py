import pygame
import constants
from logger import log_state

pygame.init()

def main():

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT));

    #FPS settings
    clock = pygame.time.Clock()
    dt = 0
    
    #game loop
    while True:
        log_state()

        #check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fill the screen canvas with black as background colour
        screen.fill("black")
        
        #Tick the clock to buzz for 60 fps
        delta_time_since_last_tick = clock.tick(60)
        dt = delta_time_since_last_tick / 1000


        pygame.display.flip()


if __name__ == "__main__":
    main()
