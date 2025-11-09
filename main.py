import pygame
from constants import *  
from logger import log_state
from player import *
import circleshape
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()            
    Player.containers = (updatable,drawable) 


    player = Player(x,y)
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    dt = 0
   
    
    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group,updatable,drawable)
    AsteroidField.containers = (updatable, )
    
    comet = AsteroidField() 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        clock.tick(60)
        dt = (clock.tick(60) / 1000)
        
        screen.fill("black")
        updatable.update(dt)
        
        #player.draw(screen)
        for thing in drawable: 
            thing.draw(screen)

        pygame.display.flip()
    

if __name__ == "__main__":
    main()
