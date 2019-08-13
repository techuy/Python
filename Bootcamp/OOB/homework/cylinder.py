import math
class Cylinder:
    
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.h = height
        self.r = radius
        
    def volume(self):
        self.sqrtR = self.r ** 2
        return self.pi*self.sqrtR*self.h
    
    def surface_area(self):
        A1 = 2 * self.pi * self.r
        A2 = self.h + self.r
        return A1*A2

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())

