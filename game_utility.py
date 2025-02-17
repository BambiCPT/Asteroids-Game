import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def restart(updatable, drawable, asteroids, shots, player, asteroid_field, score):
    updatable.empty()
    drawable.empty()
    asteroids.empty()
    shots.empty()

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    score = 0
    return asteroid_field, player, score