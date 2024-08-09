#@property decorator indicates the getter decorator.
#This will covert the function in an attribute.
#Getter on lets the output value's display and no editing is permitted by it.

class Worker:
    company="XYZ"
    salary=950000
    salarybonus=500000

    @property
    def totalamount(self):
        return self.salary + self.salarybonus
    
w=Worker()
print(w.totalamount)