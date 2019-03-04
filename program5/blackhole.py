# Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,2*Black_Hole.radius,2*Black_Hole.radius)

    def contains(self, xy):
        return self.distance(xy) <= self._width/2
    
    def update(self,model):
        eaten = set()
        for s in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(s.get_location()):
                eaten.add(s)
        for s in eaten:
            model.remove(s)
        return eaten
    
    def display(self, the_canvas):
        w,h = self.get_dimension()
        the_canvas.create_oval(self._x-w/2, self._y-h/2, self._x+w/2, self._y+h/2, fill = "black")
        