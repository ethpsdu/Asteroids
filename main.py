import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

# Main Functional
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (update_group, draw_group, asteroid_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (shot_group, update_group, draw_group)
    asteroid_field = AsteroidField()
    
    
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatatable in update_group:
            updatatable.update(dt)
        for asteroids in asteroid_group:
            if asteroids.collision_check(player):
                    print("Game over!")
                    sys.exit()
        
        screen.fill("black")
        for drawable in draw_group:
            drawable.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
        
# Can only be called if run directly
if __name__ == "__main__":
    main()