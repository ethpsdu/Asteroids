import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *
from player import *

# Main Function
def main():
    pygame.init()
    
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatatable in update_group:
            updatatable.update(dt)
        
        screen.fill("black")
        for drawable in draw_group:
            drawable.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
        
# Can only be called if run directly
if __name__ == "__main__":
    main()