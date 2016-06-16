# GUI-based version of RPSLS
# My CodeSkulptor URL: http://www.codeskulptor.org/iipp-practice-experimental/#user41_SPZH0e8GZVCcTrd.py
###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
def name_to_number(name):
    """
    Converts name input to number b/t 0 and 4. 
    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors
    """

    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        return False


def number_to_name(number):
    """
    Converts number b/t 0 and 4 into corresponding name as a string.
    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors
    """

    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        print "Number is out of range."
    

def rpsls(player_choice): 
        
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    result = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if (result == 0):
        print "Player and computer tie!"
    elif (result == 1 or result == 2):
        print "Player wins!"
    elif (result == 3 or result == 4):
        print "Computer wins!"
    else:
        print "Oops! Something went wrong. Please try again!"
        
    # print a blank line to separate consecutive games
    print 
    
# Handler for input field
def get_guess(guess):
    if (name_to_number(guess) == False):
        print "Error: Bad input \""+ guess +"\" to rpsls"
        print
        return
    else:
        rpsls(guess)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
