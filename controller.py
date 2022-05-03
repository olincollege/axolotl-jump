#capturing and handling any user intputs
import pygame
events = pygame.event.get()


class Controller():
        
        
    def __init__(self):
        self.restartGame = False
        self.quitGame = False

    def restart(self):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    self.restartGame = True

    def quit(self):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quitGame = True

class CharacterController():
    

    def __init__(self):
        self.isJumping = False

    def jumping(self):
        for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or pygame.K_UP:
                        self.isJumping = True

# Class Controller
#     Def restart
#       keyboard input to run restart function

#     Class CharacterController (Controller)
#         Init
#         Keyboard controls (Space, up, down)

#     Def get_user_input
