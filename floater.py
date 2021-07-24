# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


##from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
from random import uniform


class Floater(Prey):
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 5, 5)
        self.randomize_angle()
        self._radius = 5
        self._color = "red"

    def update(self, model):

        if random() <= .3:
            ''' randomizes angle 30% of the time by .5 increments, speed as well, but speed has to be greater than 3 speed and less than  7'''
            self._angle = self._angle + uniform(-.5, .5)
            speed = self._speed + uniform(-.5, .5)
            if speed > 3 and speed < 7:
                self._speed = speed
        self.move()
        self.wall_bounce()

    def display(self, canvas):
        canvas.create_oval(self._x-self._radius      , self._y-self._radius,
                                self._x+self._radius, self._y+self._radius,
                                fill=self._color)
