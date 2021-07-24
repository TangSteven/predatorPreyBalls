

import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from prey       import Prey
from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter

import math
import random
# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
simultons = set()
global next_one

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons
    running = False
    cycle_count = 0
    simultons = set()


#start running the simulation
def start ():
    global running
    running = True



#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just 1 update in the simulation
def step ():
    for s in simultons:
        s.update()


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global next_one
    next_one = eval(kind)

# remove simulton s from the simulation    
def Remove(x, y):
    global simultons
    cords = [x,y]
    copy = simultons.copy()
    for s in simultons:
        if s.contains(cords):
            copy.remove(s)
    simultons = copy

def remove(s):
    global simultons
    copy = simultons.copy()
    copy.remove(s)
    simultons = copy

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global next_one
    if next_one == Remove: ## if the last button pressed on the gui is "Remove"
        ##print("HI")
        next_one(x,y)
    else:
        simultons.add(next_one(x, y ))
    


#add simulton s to the simulation
def add(s):
    simultons.add(s)
    


    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    found = set()
    for s in simultons:
        if (isinstance(s, Prey)):
            found.add(s)##finds all prey, now i need to find all prey that is in a blackhole
    return found


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count = cycle_count + 1
        for s in simultons:
            s.update(model)


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    global simultons
    controller.the_canvas.delete("all")
    for s in simultons:
        s.display(controller.the_canvas)
    controller.the_progress.config(text=str(len(simultons))+" balls/"+str(cycle_count)+" cycles")
        
