"""
Capturing and handling any user intputs
"""
import pygame

class Controller():
    """
    Representation of keyboard inputs for endless runner game.
    """
    def __init__(self):
        self.restartGame = False
        self.quitGame = False
        self.isJumping = False

    def update(self):
        """
        
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.restartGame = (event.key == pygame.K_RETURN)
                self.quitGame = (event.key == pygame.K_ESCAPE)
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    self.isJumping = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    self.isJumping = False
                self.restartGame = False
                self.quitGame = False
