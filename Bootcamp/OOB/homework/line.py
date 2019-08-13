class Line:
    def __init__(self,cordi1,cordi2):
        self.cordi1 = cordi1
        self.cordi2 = cordi2

        self.deltaX=  (cordi2[0]-cordi1[0])
        self.deltaY=  (cordi2[1]-cordi1[1])

    def distance(self):
        a = self.deltaY**2
        b = self.deltaX**2
        c = b + a
        return c**0.5

    def slope(self):
        return self.deltaY/self.deltaX

coordinate1 = (3,2)
coordinate2 = (8,10)
    
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())
        