import circleshape
import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape
from constants import *
from logger import log_event
from random import *
import random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
        
    def update(self, dt):
      self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        log_event("asteroid_split")
        astro_movement = random.uniform(20,50)
        astro_one = self.velocity.rotate(astro_movement)
        astro_two = self.velocity.rotate(-astro_movement)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_astroid_one = Asteroid(self.position.x, self.position.y,new_radius)
        new_astroid_two = Asteroid(self.position.x, self.position.y,new_radius)
        new_astroid_one.velocity = astro_one * 1.2
        new_astroid_two.velocity = astro_two * 1.2


