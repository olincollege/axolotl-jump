"""
All interactions and variables that are updated and changed over the course
of the game.
"""
import random

scr_size = (width,height) = (600,600)
FPS = 60
GRAVITY = 0.6

class Model():
    """
    Model of Endless Runner Game.
    """
    def __init__(self):
        self.characterpos = [0, 0]
        self.score = 0
        self.obstacles = [Obstacle(30, 200)]
        self.isDead = False
        self.y_change = 0

    def collision(self, obstacle):
        """
        Function takes an obstacle and determines whether or not a
        collision has occured.

        Args:
            obstacle: an object with a given size and position.
        """
        if abs(obstacle.position - self.characterpos[0]) <= 15 and \
            self.characterpos[1] <= obstacle.size:
            return True
        return False

    def update(self, jumping):
        """
        Function updates variables as time passes. It includes jumping,
        generating obstacles, the position of obstacles, and collision
        detection.

        Args:
            jumping: Boolean value (True/False) of whether or not the character
            is jumping.
        """
        if self.isDead is False:
            # increase score
            self.score += 1

            # generate obstacles
            while self.obstacles[-1].position < 2000:
                last_position = self.obstacles[-1].position
                random_position = random.randrange(100, 300)
                self.obstacles.append(Obstacle(30, last_position + \
                    random_position))

            for obstacle in self.obstacles:
                # update position of obstacles
                obstacle.position -= 2 + self.score//1000
                # detect collision
                if self.collision(obstacle):
                    self.isDead = True

            if jumping is True and self.y_change == 0 and self.characterpos[1]\
                == 0:
                self.y_change = 12

            # jump physics
            if self.y_change > 0 or self.characterpos[1] > 0:
                self.characterpos[1] += self.y_change
                self.y_change -= GRAVITY
            if self.characterpos[1] < 0:
                self.characterpos[1] = 0
            if self.characterpos[1] == 0 and self.y_change < 0:
                self.y_change = 0

class Obstacle():
    """
    Representation of the obstacles.
    """
    def __init__(self, size, position):
        self.size = size
        self.position = position
