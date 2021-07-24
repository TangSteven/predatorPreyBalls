# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey

class Pulsator(Black_Hole):
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self._counter = 50
    
    def update(self, model):
        self._counter = self._counter -1
        if self._counter == 0:
            model.remove(self)
        eaten = set()
        for prey in model.find(Prey):
            cords = [prey._x, prey._y]
            if self.contains(cords):
                model.remove(prey)
                eaten.add(prey)
                self._radius = self._radius + 1
                self._counter = 50
        return eaten