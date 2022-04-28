import pygame
from pygame.locals import *

pygame.init()

scr_size = (width,height) = (600,600)
FPS = 60
gravity = 0.6

high_score = 0

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Mushroom Run")

class Character(pygame.sprite.Sprite):
    def __init__(self):
        # is this supposed to be super?
        self.surf = pygame.Surface(())
        self.surf.fill(())
        self.rect = self.surf.get_rect(center = (10,420))   
        self.index = 0
        self.counter = 0
        self.score = 0

        self.isJumping = False
        self.isDead = False
        self.movement = [0,0]
        self.jumpSpeed = 11.5

    def draw(self):
        screen.blit(self.rect)

    def checkbounds(self):
        if self.rect < int(0.98*height):
            self.rect = int(0.98*height)
            self.isJumping = False

    def update(self):
        if self.isJumping:
            self.movement[1] = self.movement[1] + gravity

        if self.isJumping:
            self.index = 0
        
        if self.isDead:
            self.index = 4

        self.rect = self.rect.move(self.movement)
        self.checkbounds() 


#    Init
#         Location
#         Dead or alive
#         Sprite
