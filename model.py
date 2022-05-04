import controller
import character
import game

scr_size = (width,height) = (600,600)
FPS = 60
gravity = 0.6

class Model():


    def __init__(self):
        self.characterpos = [0,0]
        self.score = 0
        self.obstacles = [Obstacle(30, 30)]
        self.isDead = False

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

            for i in range(30):
                # generate obstacles
                last_position = self.obstacles[-1].position
                self.obstacles.append(Obstacle(30, last_position + 200))

            for obstacle in self.obstacles:
                # update position of obstacles
                obstacle.position -= 1
                # detect collision
                if abs(obstacle.position - self.characterpos[0]) <= 15 and self.characterpos[1] <= obstacle.size:
                    self.isDead = True 

            if jumping == True:
                self.characterpos[1] = 40
            else:
                self.characterpos[1] = 0
            

class Obstacle():

    def __init__(self, size, position):
        self.size = size
        self.position = position