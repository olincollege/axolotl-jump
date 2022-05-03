import pygame
import controller
import character
import game

scr_size = (width,height) = (600,600)
FPS = 60
gravity = 0.6

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Mushroom Run")

class Model():


    def __init__(self):
        self.characterpos == [0,0]

    def jump(self):
        if controller.CharacterController.isJumping == True:
            self.characterpos[1] = self.characterpos[1] + gravity

    def restart_game(self):
        if controller.Controller.restartGame == True:
            return game
        
    def exit(self):
        if controller.Controller.quitGame == True:
            quit()
    
    def game_over(self):
        if character.Character.isDead == True:
            print("Game Over: Press Enter to Restart and ESC to quit.")

    def update(self):
        pass