#This syntax is known by the name of class method
#This code changes the class attribute by not even amending the class attributes
#We can change the class attribute only by making the instance attribute with the desired changed attribute value

class worker:
    Company="XYZ"
    Location="Work  From Home"
    
    def edit(self,loc):
        self.__class__.Location=loc

w=worker()
print(worker.Location)
w.edit("Head Office")
print(w.Location)
print(worker.Location)


