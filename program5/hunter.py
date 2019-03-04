# Hunter is derived from Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        w,h = self.get_dimension()
        Mobile_Simulton.__init__(self,x,y,w,h,0,5)
        self.randomize_angle()
        
    def update(self,model):
        eaten = Pulsator.update(self,model)
        preys = model.find(lambda x: isinstance(x, Prey) and self.distance(x.get_location())<=200)
        if len(preys) > 0:
            nearest, goal = min([(self.distance(s.get_location()),s) for s in preys])
            sx,sy = self.get_location()
            x,y = goal.get_location()
            self.set_angle(atan2(y-sy, x-sx))
        self.move()
        return eaten
            
