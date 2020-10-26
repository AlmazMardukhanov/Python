class Point:
    x=""
    y=""
    def setx(self,newx):
        self.x=newx
    def sety(self,newy):
        self.y=newy
    def getx(self):
        print(self.x)
    def gety(self):
        print(self.y)

point=Point()
point.setx(5)
point.sety(6)
point.getx()
point.gety()
