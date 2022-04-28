
'''The Game Loop is where all the game events occur, update and get drawn to 
the screen. Once the initial setup and initialization of variables is out of 
the way, the Game Loop begins where the program keeps looping over and over 
until an event of type QUIT occurs.'''

class Game:
#     Init
#     clock/time
#     Framerate
#     Score (based on time)
# Def update board
# Def update characters
#     Update character position based on current location
# Def game_over


#exiting the game loop
    while True:
        pygame.display.update() #rerenders screen at each loop iteration
        for event in pygame.event.get():
            pygame.quit()
            sys.exit()
