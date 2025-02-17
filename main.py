import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("/home/bambino/Workspace/github.com/BambiCPT/Asteroids/AsteroidsBackground.jpg")
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    font = pygame.font.Font(None, 36)
 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    

    while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 print(f"{score}")
                 return
         
         screen.blit(background_image, (0, 0))
         updatable.update(dt)

         for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                print(f"{score}")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    score += asteroid.points()
                    
         score_text = font.render(f"Score: {score}", True, "white")
         screen.blit(score_text, ((1270 - score_text.get_width()), 10))

         for obj in drawable:
             obj.draw(screen)

         pygame.display.flip()  

         dt = clock.tick(60) / 1000

         

if __name__ == "__main__":
    main()

