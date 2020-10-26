class Animal:
    name=""
    def eat(self):
        print('Ням-ням')
    def setName(self,newName):
        self.name=newName
    def getName(self):
        print(self.name)
    def makeNoise(self):
        print(self.name+" говорит Грр")
    def __init__(self,newName):
        self.name=newName
        print('Родилось животное: '+self.name)

mydog=Animal('Шарик')
mydog.eat()
mydog.getName()
mydog.setName('Вася')
mydog.getName()
mydog.makeNoise()



