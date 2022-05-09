
'''The Game Loop is where all the game events occur, update and get drawn to 
the screen. Once the initial setup and initialization of variables is out of 
the way, the Game Loop begins where the program keeps looping over and over 
until an event of type QUIT occurs.'''

import pygame
import model
import controller
import sys

pygame.init()

scr_size = (width,height) = (1000,600)
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (1000,600))

image = pygame.image.load("stalactites.png")
image = pygame.transform.scale(image, (30, 80))

character_image = pygame.image.load("axolotl.png")
character_image = pygame.transform.scale(character_image, (50, 50))

ground = 100


class Game:
    """
    Representation of the view and game of the endless runner game.
    """
    def __init__(self):
        self.screen = pygame.display.set_mode(scr_size)
        self.model = model.Model()
        self.controller = controller.Controller()
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.highscore = 0

    def draw_character(self, position):
        # rectangle = pygame.Rect(250 + position[0] - 10, 500 - position[1] - 40, 20, 40)
        # pygame.draw.rect(self.screen, (250,50,50), rectangle)
        self.screen.blit(character_image, (250 + position[0] - 10, 500 - position[1] - 40))

    def draw_obstacle(self, position, size):
        # rectangle = pygame.Rect(250 + position - 5, 440 + size, 10, size)
        # pygame.draw.rect(self.screen, (0,0,50), rectangle)
        self.screen.blit(image, (250 + position - 5, 400 + size))

    def update(self):
        self.screen.fill((10,0,20))
        self.screen.blit(bg,(0,0))
        self.controller.update()
        self.model.update(self.controller.isJumping)

        # draw floor
        pygame.draw.rect(self.screen, (50,50,120), [0,500,width,100])

        # draw character
        self.draw_character(self.model.characterpos)
        # draw obstacles
        for obstacle in self.model.obstacles:
            self.draw_obstacle(obstacle.position, obstacle.size)

        # update score
        self.clock.tick(self.fps)
        font = pygame.font.SysFont("roboto", 30)
        score_text = font.render(f"Score: {self.model.score}", True, (250,250,250))
        text_rect = score_text.get_rect(center = (width/2, 100))
        self.screen.blit(score_text, text_rect)
        pygame.display.flip()

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
        font = pygame.font.SysFont("roboto", 50)
        text = font.render(f"Game Over: Press Enter to Restart", True, (250,250,250))
        
        self.highscore = max(self.model.score, self.highscore)
        font1 = pygame.font.SysFont("roboto", 30)
        text1 = font1.render(f"Highscore: {self.highscore}", True, (250,250,250))
        
        text_rect = text.get_rect(center = (width/2, height/2))
        text1_rect = text1.get_rect(center = (width/2, height/2 - 50))

        self.screen.blit(text, text_rect)
        self.screen.blit(text1, text1_rect)
        pygame.display.flip()


#exiting the game loop
    # while True:
    #     pygame.display.update() #rerenders screen at each loop iteration
    #     for event in pygame.event.get():
    #         pygame.quit()
    #         sys.exit()
