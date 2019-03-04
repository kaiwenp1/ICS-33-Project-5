import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
#from concurrent.futures._base import RUNNING
#from _tracemalloc import stop


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
#balls = set()
simultons = set()
stop_after_one = False
object_clicked = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons, stop_after_one
    running = False
    cycle_count = 0
    simultons = set()
    stop_after_one = False


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global runnig, stop_after_one
    running = True
    stop_after_one = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_clicked
    object_clicked = kind

#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if object_clicked == None:
        print("Select an object first.")
    elif object_clicked == "Remove":
        for s in find(lambda s: s.contains((x,y))):
            simultons.remove(s)
    else:
        simultons.add(eval(object_clicked+"("+str(x)+","+str(y)+")"))
    #balls.add(Ball(x,y,random_speed(),random_angle(),random_color()))


#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return {s for s in simultons if p(s)}


#call update for every simulton in the simulation
def update_all():
    global running
    global stop_after_one
    global cycle_count
    if running:
        #global cycle_count
        #global world
        cycle_count += 1
        copy_simultons = set(simultons)
        for s in copy_simultons:
            if s in simultons:
                s.update(model)
        if stop_after_one:
            running = False
            stop_after_one = False


#delete each simulton in the simulation from the canvas; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    for s in simultons:
        s.display(controller.the_canvas)
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(simultons))+" simultons")
