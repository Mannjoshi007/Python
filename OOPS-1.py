#Object Oriented Programming is a way useful for segration and sepration of various content on the particular specified basis
#We make Class for separation of the content
#Self is the keyword which gets substituted by the name of the object created
#Here, num is the Object created for the Class Total
#Self can be taken as a compulsory argument to be given for a function in OOPS
#We can have functions/methods in a Class too

class Total:
    def sum(self):
        return self.a + self.b
    
num=Total()
num.a=2
num.b=3
s=num.sum()

print(s)