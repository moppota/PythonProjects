#following tutorial trying to learn pygame
import pygame 

from pygame.locals import (

    K_UP, # initialising key inputs I need
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

screen.fill((255,255,255))

surf = pygame.Surface((50,50))

surf.fill((0,0,0))

rect = surf.get_rect()

surf_centre = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_width())/2
)

screen.blit(surf, surf_centre)   
pygame.display.flip()

while running:

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type == QUIT:
            running = False