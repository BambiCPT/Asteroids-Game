import pygame
import random
import math
from constants import *
from circleshape import CircleShape

def generate_asteroid_surface(radius, points=12):
    vertices = []
    for i in range(points):
        angle = 2 * math.pi * i / points
        distance = radius + random.randint(-5, 5)
        vertices.append((radius + math.cos(angle)*distance, radius + math.sin(angle) * distance))
        
    surface = pygame.Surface((radius *2, radius * 2), pygame.SRCALPHA)
    pygame.draw.polygon(surface, ("white"), vertices, 2)
    return surface
 
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = generate_asteroid_surface(radius)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            A1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            A2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            A1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            A2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
            
    def draw(self, screen):
        screen.blit(self.image, self.position - pygame.math.Vector2(self.radius, self.radius))

    def update(self, dt):
        self.position += (self.velocity * dt)

    def points(self):
        if self.radius == ASTEROID_MAX_RADIUS:
            return 3
        elif self.radius == ASTEROID_MIN_RADIUS:
            return 1
        elif self.radius < ASTEROID_MAX_RADIUS and self.radius > ASTEROID_MIN_RADIUS:
            return 2
        



