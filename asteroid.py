import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        rand_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        vect1 = self.velocity.rotate(rand_angle)
        vect2 = self.velocity.rotate(-rand_angle)
        new_raidus = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_raidus)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_raidus)
        new_asteroid1.velocity = vect1 * 1.2
        new_asteroid2.velocity = vect2 * 1.2