import random
import controller
import character
import game

scr_size = (width,height) = (600,600)
FPS = 60
gravity = 0.6

class Model():


    def __init__(self):
        self.characterpos = [0, 0]
        self.score = 0
        self.obstacles = [Obstacle(30, 200)]
        self.isDead = False
        self.y_change = 0

    def restart_game(self):
        if controller.Controller.restartGame == True:
            return game
        
    def exit(self):
        if controller.Controller.quitGame == True:
            quit()
    
    def game_over(self):
        if self.isDead == True:
            print("Game Over: Press Enter to Restart and ESC to quit.")

    def update(self, jumping, reset, exit):
        if self.isDead == False:
            self.score += 1

            for i in range(6):
                # generate obstacles
                last_position = self.obstacles[-1].position
                random_position = random.randrange(100, 300)
                self.obstacles.append(Obstacle(30, last_position + random_position))

            for obstacle in self.obstacles:
                # update position of obstacles
                obstacle.position -= 2 + self.score//1000
                # detect collision
                if abs(obstacle.position - self.characterpos[0]) <= 15 and self.characterpos[1] >= obstacle.size:
                    self.isDead = True 

            if jumping == True and self.y_change == 0:
                self.y_change = 12

            # jump physics
            if self.y_change > 0 or self.characterpos[1] < 30:
                self.characterpos[1] -= self.y_change
                self.y_change -= gravity
            if self.characterpos[1] > 30:
                self.characterpos[1] = 30
            if self.characterpos[1] == 30 and self.y_change < 0:
                self.y_change = 0

            # if self.score % 1000 == 0 and self.score != 0:
            #    level = self.score / 1000
                
            

class Obstacle():

    def __init__(self, size, position):
        self.size = size
        self.position = position