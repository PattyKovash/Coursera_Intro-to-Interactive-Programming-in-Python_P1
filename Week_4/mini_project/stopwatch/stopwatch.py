# "Stopwatch: The Game"

import simplegui

# define global variables
WIDTH = 500
HEIGHT = 300
count = 0
success = 0
stops = 0
is_on = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    seconds = int(t * .1)
    a = seconds // 60
    b = int((t * .1) - (60 * a)) // 10
    c = seconds % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_on
    if (not is_on):
        timer.start()
        is_on = True
    
def stop():
    global is_on, stops, success
    if (is_on):
        timer.stop()
        is_on = False
        stops += 1
        if (count % 10 == 0):
            success += 1
    
def reset():
    global count, success, stops, is_on
    count = 0
    success = 0
    stops = 0
    is_on = False

# define event handler for timer with 0.1 sec interval
def watch():
    global count, success
    count += 1   

# define draw handler
def display(canvas):
    global success
    canvas.draw_text(format(count), [68, 195], 130, "#808080", "sans-serif")
    canvas.draw_text("Success: " + str(success) + " / " + "Stops: " + str(stops), [WIDTH - 170, 30], 15, "#808080", "sans-serif")


    
# create frame & timer
frame = simplegui.create_frame("Stopwatch", WIDTH, HEIGHT)
frame.set_canvas_background("#F5FFFA")
timer = simplegui.create_timer(100, watch)

# add buttons
frame.add_button("START", start, 200)
frame.add_button("STOP", stop, 200)
frame.add_button("RESET", reset, 200)

# register event handlers
frame.set_draw_handler(display)

# start frame 
frame.start()
