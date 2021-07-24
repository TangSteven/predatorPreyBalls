# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 5, 5, 10, 10)
        self.randomize_angle()
        self._speed = 5
        self._viewdistance = 200

    def update(self, model):
        self.move()
        self._counter = self._counter -1
        if self._counter == 0:
            model.remove(self)
        eaten = set()
        for prey in model.find(Prey):
            cords = [prey._x, prey._y]
            if self.distance(cords) <= 200:
                ##print("CHASING")
                self._angle = atan2(prey._y - self._y, prey._x - self._x)
            if self.contains(cords):
                model.remove(prey)
                eaten.add(prey)
                self._radius = self._radius + 1
                self._counter = 30
        return eaten
