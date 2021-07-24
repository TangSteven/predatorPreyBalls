# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
        self._color = "black"
        self._radius = 10
        

    def update(self, model): 
        '''returns a set of removed simultons'''
        
        eaten = set()
        for prey in model.find(Prey):
            cords = [prey._x, prey._y]
            if self.contains(cords):
                model.remove(prey)
                eaten.add(prey)

        

        return eaten
        


    def contains(self,xy): 
        ''' finds if the coordinates(center) is in the blackhole's radius'''
        return (self.distance(xy) < self._radius)
            

    def display(self, canvas):
        canvas.create_oval(self._x - self._radius, self._y - self._radius,
                            self._x+self._radius, self._y +self._radius,
                            fill = self._color)
    