# Axolotl Jump
Axolotl Jump is an endless runner game that features an axolotl trying to jump over stalagmites in a cave. The goal of the game is to set the highscore and see how far you can get!

In order to replicate this game, you will first need to be running python 3, and you need to install pygame. To do this, you can use the following command in your terminal:

'''pip install pygame'''

Look at [our website](https://olincollege.github.io/axolotl-jump/) for more info!

## model.py
After setting up, we can start with the model.py file. This is the most important file, as it contains the state of the program. In this file, we will store a few important things: This includes the position of the character, the position of the obstacles and the score. In our init function, we should list all of these variables, along with any supporting variables, such as whether or not the character is dead or the change in y position for the character.

Next, we need a function that detects any collisions. This can be done by calcuting the distance between the the character and the obstacle and constructing an if statement that returns True or False, depending on if the character and obstacle has made contact.

Then, we can create the update function, which will contain the updates of everything else. First of all, this function will increase the score every time it updates. Then, it will also generate obstacles in a while loop, only if the obstacle is within 1000 pixels off screen so it doesn't create too many obstacles. It will then choose a random position within 100 to 300 pixels to place a obstacle behind the previous one. The next part of this function will move the obstacles over towards the character. This speed is also dependent on the score. The game will increase the speed of the obstacle every 1000 points. Next, we run the collision function that we wrote above. The following part of this update function is to check whether or not our character is jumping. If the character is mid jump, the the character will not jump again. It will only jump when the y position is 0, and jumping is set to be True. Then we added some additional if statements that allows the character to have smooth jump physics.

Finally, we must create an Obstacle class within model. Since we are constantly creating new obstacles and changing their position, creating an obstacle class that takes in size and position as it's arguments will allow us to create as many obstacle objects we will need for this game.

## controller.py
After creating the guts of the game, we can start taking in keyboard inputs. We need to initialize our 3 main keyboard interactions: jumping, which is spacebar or up arrow, exit, which is escape, and enter, which is play again. Using pygame documentation, you can easily figure out the code for each key, and set the variables to either True or False, based on whether or not you are pressing the key.

## game.py
Now it's time to visualize everything and see it on a screen. In this file, we must import sys, pygame, model.py, and controller.py. If you'd like to represent your character, obstacle, or background as an image, you can load them into pygame in the beginning of this file. You can also resize these images. This file will require you to heavily reference pygame documentation.

We need to add the screen, model, controller, fps, clock, and highscore in the init function in order to display all of our elements.

Then, we can create a function that draws the character onto the board. This is done by using screen and blit.

Along with that, we can create a function that also draws the obstacles onto the board using screen.

In our update function, we can start drawing elements onto the screen now. First, we can draw the background. Then, we can update the model and controller. We can also draw the floor. Then we can run the functions we just created to draw both the character and obstacle onto the screen. Finally, we can write the score on the top of the screen and continuously update it.

Now that the update function is done, we can create a function to start the game. This will just run update function until the character dies, then it will run the game over function. You are also given the option to restart or exit by pressing enter or esc in the game over phase.

The final function will be the game over function. This function shows us our highscore and a message saying "Game Over: Press Enter to Restart." 

## main.py
Finally, the main file will initialize the game and run the start game function in game, which will cause the game to run and display on your screen.
