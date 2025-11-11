import pygame
from constants import *  
from logger import log_state
from player import *
import circleshape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()            
    Player.containers = (updatable,drawable) 


    player = Player(x,y, PLAYER_SHOOT_COOLDOWN_SECONDS)
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    dt = 0
   
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable, )
    shot = pygame.sprite.Group()
    comet = AsteroidField()
    shots = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable) 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        clock.tick(60)
        dt = (clock.tick(60) / 1000)
        
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                
                


        if player.cooldown > 0: 
            player.cooldown -= dt     
        #player.draw(screen)
        for thing in drawable: 
            thing.draw(screen)

        pygame.display.flip()
     

if __name__ == "__main__":
    main()
