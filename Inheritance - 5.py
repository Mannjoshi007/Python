#Super() method allows to have the output of the method of the paren class in the method of the child class too.
#This will work for same as well as different method names
#It is not for attributes

class man:
    def breathing(Self):
        print("The man is breathing.")

class child(man):
    def breathing(Self):
        super().breathing()
        print("There is a nice environment.")

m=man()
c=child()
m.breathing()
c.breathing()
