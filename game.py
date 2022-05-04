
'''The Game Loop is where all the game events occur, update and get drawn to 
the screen. Once the initial setup and initialization of variables is out of 
the way, the Game Loop begins where the program keeps looping over and over 
until an event of type QUIT occurs.'''

import pygame
import model
import controller
import sys

pygame.init()

scr_size = (width,height) = (600,600)

class Game:
#     Init
#     clock/time
#     Framerate
#     Score (based on time)
# Def update board
# Def update characters
#     Update character position based on current location
# Def game_over
    def __init__(self):
        self.screen = pygame.display.set_mode(scr_size)
        self.model = model.Model()
        self.controller = controller.Controller()
        self.fps = 60
        self.clock = pygame.time.Clock()

    def draw_character(self, position):
        rectangle = pygame.Rect(100 + position[0] - 10, 500 - position[1]-40, 20, 40)
        pygame.draw.rect(self.screen, (0,0,0), rectangle)

    def draw_obstacle(self, position, size):
        rectangle = pygame.Rect(100 + position - 5, 500-size, 10, size)
        pygame.draw.rect(self.screen, (0,0,0), rectangle)

    def update(self):
        self.screen.fill((250,250,250))
        self.controller.update()
        self.model.update(self.controller.isJumping ,self.controller.restartGame, self.controller.quitGame)

        self.draw_character(self.model.characterpos)
        for obstacle in self.model.obstacles:
            self.draw_obstacle(obstacle.position, obstacle.size)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def start(self):
        self.model = model.Model()
        while self.model.isDead == False:
            self.update()
    
        self.game_over()
        while True:
            self.controller.update()
            if self.controller.quitGame:
                sys.exit(0)
            elif self.controller.restartGame:
                self.start()
            
    def game_over(self):
        font = pygame.font.SysFont("roboto", 30)
        text = font.render("Game Over", True, (0,0,0))
        text_rect = text.get_rect(center = (width/2, height/2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()


#exiting the game loop
    # while True:
    #     pygame.display.update() #rerenders screen at each loop iteration
    #     for event in pygame.event.get():
    #         pygame.quit()
    #         sys.exit()
