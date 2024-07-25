#Abstraction means the layering the inner working content of the class
#Encapsulation is the separation of methods/functions for a particulartask in the specific class way
#Method names are written in camelCase 
#camelCase means to write the starting letter of the first word as small and then the starting letters of all other following words as capial

class Remote:
    def moveForward(self):
        pass
    def moveBackward(self):
        pass

class Player:
    def move(self):
        pass
    def turn(self):
        pass

r1=Remote()
p1=Player()

if(r1.moveForward()):
    p1.move()