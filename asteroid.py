from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()    
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        v1_vect = self.velocity.rotate(rand_angle)
        v2_vect = self.velocity.rotate(-rand_angle)
        newrad = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x,self.position.y,newrad)
        asteroid_1.velocity = v1_vect * 1.2
        asteroid_2 = Asteroid(self.position.x,self.position.y,newrad)
        asteroid_2.velocity = v2_vect * 1.2
