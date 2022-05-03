import pygame
from pygame.locals import *

scr_size = (width,height) = (600,600)
FPS = 60
gravity = 0.6

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Mushroom Run")

# class 
# init
    # position of everything
    # obstacle position
    # size of obstacles
    # score (time passed)
    # game state (game over/restart)
# 

class Map():
    def __init__(self):
        self.surf = pygame.Surface(())
        self.surf.fill(())
        self.rect = self.surf.get_rect(center = (10,420))   

class Ground():
    def __init__(self, speed = -5):
        self.surf = pygame.Surface(())
        self.surf.fill(())
        self.rect = self.surf.get_rect(center = (10,420))   
        self.speed = speed

    def draw(self):
        screen.blit(self.rect)

    def update(self):
        self.rect += self.speed

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface(())
        self.surf.fill(())
        self.rect = self.surf.get_rect(center = (10,420))
        self.movement = [5, 0]

    def draw(self):
        screen.blit(self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect < 0:
            self.kill()
