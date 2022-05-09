# Goal of the Game

In Axolotl Jump, your goal is to accumulate the highest score by jumping over as many moving stalagmites as possible. 

# Project Goal

We were inspired by platformer games and the artstyles of Ori Will of the Wisps and Hollow Knight. We wanted to create a game that was simple to play and incorporated pretty visuals.

# Game Overview

Axolotl Jump begins with the main character, The Axolotl, on the left side of the screen. The game is initiated when the main.py file is run. Once the game begins, stalagmites start moving right to left towards the player. To avoid the stalagmites, the player uses either the spacebar or the up arrow key to jump. For every 1000 points, the speed of the obstacles will increase by one frame per second. The game ends when the character collides with one of the stalagmites.

# Game Demo
<figure class="video_container">
  <iframe src="https://youtu.be/7keMX7XQP-k" frameborder="0" allowfullscreen="true"> </iframe>
</figure> 

# Game Components

At the top of the screen the current score of the play is displayed.
![The player's score is visible at the top center of the screen.](/img/axolotl_jump_in_game_screen.png)

When the game ends, the highest score a player has gotten playing the game will be displayed. This stat is updated for every new game play and will be overwritten if the current player's score is greater than the previous player's score. 
![Large text reading "Game Over" is displayed, alongside the player's current score and the high score for the game](/img/axolotl_jump_game_over_screen.png)

# Character
![A pink goofy axolotl](/img/axolotl.png)

The main character of Axolotl Jump is a pink axololt. The spacebar or the up arrow key can be pressed to get The Axolotl to jump.

# Obstacles

![A blue stalagmite](/img/stalactites.PNG)

The obstacles of Axolotl Jump are stalagmites, which move along the floor of the cave. The distance between the stalagmites is randomized to the timing of when a player will need to jump is unpredictable.

# Installation Instructions

To play this game, you will need to instaill python and pygame, and download all the files in the [axolotl-jump repository](https://github.com/olincollege/axolotl-jump). Refer to the [README](https://github.com/olincollege/axolotl-jump/blob/main/README.md) on our github page for detailed installation instructions.

# About Us

This game was created by Jen Lee '23 and Luke Milroy '23. Jen is a design major and Luke is a robotics major at Olin College of Engineering. 

# Attributions

We looked to this [tutorial](https://www.youtube.com/watch?v=ZV8TNrwqG1Y) from LeMaster Tech for inital structure development.

We utilized freepik for the images for the [background](https://www.freepik.com/free-vector/cave-cartoon-background-stone-tunnel-frame-with-snow-stalactites-entrance-mountain-empty-hole-rock-with-copy-space-text-image-grotto-hidden-underground-tunnel-vector-illustration_24025357.htm#page=2&query=cave&position=20&from_view=author) and the [tutorial](https://www.freepik.com/free-vector/stalactite-icicle-shaped-hanging-from-caves-ceilings-mineral-formations-varieties-cobalt-blue-realistic-set-isolated-illustration_21078356.htm#query=cave%20background&position=14&from_view=search). 
