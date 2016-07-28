# Implementation of classic arcade game Pong

# In my implementation, I wanted to allow the ball to hit
# the corners of paddles. To do this, I calculated the distance
# between the ball position and the paddle position (gutter side)
# when the ball reaches the gutters.After careful examination,
# I determined the distance range of [0, 50) to be best. 0 is the
# minimum distance and 50 is the maximum distance allowed. A distance
# of 50 is where the very tip of the paddle corner touches the ball
# (I allow for the ball to touch the paddle and gutter at the same
# time). A distance above 50 and the ball no longer touches the paddle.
# Logically the lower bound should be the ball radius. However, 
# in this implemenation, when the ball is moving at a high velocity,
# there is a lag in calculating the position of the ball from when it 
# reaches the gutter. This can cause a distance below 20 when hitting 
# the paddle straight on.

# A pause functionality was also added to the game. 

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_pos = HEIGHT / 2
paddle2_vel = 0
score1 = 0
score2 = 0
pause = False
pause_text = ""
pause_dir = ""
vel_holder = []


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
   
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    
    ball_vel[0] += random.randrange(2, 4) 
    ball_vel[1] -= random.randrange(1, 3) 
    
    if not direction:
        ball_vel[0] = - ball_vel[0]        
    
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, pause  
    global score1, score2  
    
    paddle1_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_pos = HEIGHT / 2
    paddle2_vel = 0
    score1 = 0
    score2 = 0 
    pause = False
    spawn_ball(RIGHT)

def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, pause_text, pause_dir
    global score1, score2
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw scores
    canvas.draw_text(str(score1), [130, 90], 70, "SpringGreen", "sans-serif")
    canvas.draw_text(str(score2), [430, 90], 70, "SpringGreen", "sans-serif")

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # draw left paddle
    canvas.draw_line([0, paddle1_pos],
                     [PAD_WIDTH, paddle1_pos], PAD_HEIGHT, "White")
    
    # draw right paddle
    canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos],
                     [WIDTH, paddle2_pos], PAD_HEIGHT, "White")
    
    # draw pause status 
    canvas.draw_text(pause_text, [80, 210], 60, "SpringGreen", "sans-serif")
    canvas.draw_text(pause_dir, [65, 240], 20, "SpringGreen", "sans-serif")
    
    # update pause status
    if pause:
        pause_text = "GAME PAUSED"
        pause_dir = "(Hit SPACEBAR or click pause BUTTON to continue)"
    else:
        pause_text = ""
        pause_dir = ""
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # update left paddle's vertical position, keep paddle on the screen
    if (HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
        
    # update right paddle's vertical position, keep paddle on the screen
    if (HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    # determine whether ball collides with top & bottom walls  
    if (ball_pos[1] == BALL_RADIUS or ball_pos[1] == HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
 
    # determine whether paddle and ball collide (paddle corners included)
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) or (ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS)):
        ball_vel[0] = - ball_vel[0]
        
        # determine the distance between the ball position and the position of the paddle.  
        right_distance = int(math.sqrt((ball_pos[0] - (WIDTH - PAD_WIDTH))**2 + (ball_pos[1] - paddle2_pos)**2))
        left_distance = int(math.sqrt((ball_pos[0] - PAD_WIDTH)**2 + (ball_pos[1] - paddle1_pos)**2))

        # if distance within range, paddle & ball collide
        if (0 <= right_distance < 51) or (0 <= left_distance < 51): 
            ball_vel[0] += (ball_vel[0] * .1)    
        else:
            if left_distance > 500:
                score1 += 1
                spawn_ball(LEFT)
            else:
                score2 += 1
                spawn_ball(RIGHT)
                
        #print "****"
        #print "BREAK"
        #print "****"
        #print "ball_pos[0]: ", ball_pos[0]
        #print "distance from R: ", right_distance
        #print "distance from L: ", left_distance
        #print ball_vel
        
def keydown(key):
    global paddle1_vel, paddle2_vel, vel_holder, ball_vel, pause
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
        
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
    
    if key == simplegui.KEY_MAP["space"]:
        pause_game()
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
    if (key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0

def pause_game():
    global pause, ball_vel, vel_holder
    
    if not pause:
        vel_holder = list(ball_vel)
        ball_vel = [0, 0]
        pause = True
    else:
        ball_vel = list(vel_holder)
        pause = False

    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART", new_game, 200)
frame.add_button("PAUSE (click or space)", pause_game, 200)

# start frame
frame.start()
new_game()


