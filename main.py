import pygame
from constants import *  
from logger import log_state
from player import *
import circleshape
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        clock.tick(60)
        dt = (clock.tick(60) / 1000)
        
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()

    

if __name__ == "__main__":
    main()
