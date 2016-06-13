# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random

def powerball():
    one = str(random.randrange(1, 60))
    two = str(random.randrange(1, 60))
    three = str(random.randrange(1, 60))
    four = str(random.randrange(1, 60))
    five = str(random.randrange(1, 60))
    powerball = str(random.randrange(1, 36))
    print "Today's numbers are " + one + ", " + two + ", " + three + ", " + four + ", and " + five + ". The Powerball number is " + powerball + "." 

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
