# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import random
import simplegui

# helper function to start and restart the game
def new_game():
    """
    Function starts a new game when called. Takes no arguments.
    Does not return a value. Sets the secret number and number
    of allowed guesses. Prints new game message, the game range,
    and number of remaining allowed guesses.
    """
    
    global secret_number
    global allowed_guess
    global game_range
   
    # this condition allows the game to start immediately
    # on initial run of game. Condition checks to see if a value 
    # has been assigned to game_range. 
    if (not "game_range" in globals()):
        game_range = 100
    
    # initialize variables
    secret_number = random.randrange(0, game_range)

    # Binary search mathematical equation to determine number
    # of allowed guesses. 2**n = high_range + low_range + 1
    allowed_guess = int(math.ceil(math.log(game_range + 1) / math.log(2)))
       
    print "New game! Range is [0," + str(game_range) + ")" 
    print "Number of remaining guesses is " + str(allowed_guess)
    
# define event handlers for control panel
def range100():
    """Re-assign end range for secret number to 100"""
    
    global game_range
    game_range = 100
    print
    new_game()
      
def range1000():
    """Re-assign end range for secret number to 1000"""
    
    global game_range
    game_range = 1000
    print
    new_game()
        
def input_guess(guess):
    """Takes string input. Converts string to integer. 
    Decrements allowed_guess by 1. Checks if input matches 
    secret_number and tracks number of guesses taken. Starts
    a new game if game won or lost.
    """
    
    global allowed_guess
    print 
    
    # convert guess string to integer
    guess = int(guess)
    
    # decrement remaining guesses 
    allowed_guess -= 1
    
    print "Guess was " + str(guess)
    print "Number of remaining guesses is " + str(allowed_guess)
    
    # compare guess to secret number
    if ((allowed_guess < 1) and (guess != secret_number)):
        print "Sorry, you're out of guesses! The number was " + str(secret_number)
        print
        return new_game()        
    elif (guess == secret_number):
        print "Correct!"
        print
        return new_game()
    elif (guess > secret_number):
        print "Lower!"
    else:
        print "Higher!"                 
            
# create frame 
frame = simplegui.create_frame("Guess the Number", 250, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("What is your guess?", input_guess, 200)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
