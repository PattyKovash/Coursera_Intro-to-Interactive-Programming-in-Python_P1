# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
is_on = False


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
  
    
# Button handler
def click():
    global is_on, total_ticks
   
    if (is_on):
        timer.stop()
        is_on = False
        print total_ticks
        print "It took you " + str(total_ticks / 100.00) + " seconds!"
        total_ticks = 0
    else:
        timer.start()
        is_on = True

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
