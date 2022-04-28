import pygame
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 600
WIDTH = 800
ACC = 0.5
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(())
        self.surf.fill(())
        self.rect = self.surf.get_rect(center = (10,420))

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.surface((WIDTH, 20))
        self.surf.fill((244, 0, 0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT -10))

PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0,0,0))

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

        pygame.display.update()
        FramePerSec.tick(FPS)
