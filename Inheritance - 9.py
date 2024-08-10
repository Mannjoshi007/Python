#Setter is used to edit the value of the function is made to get converted in a property

class worker:
    company="XYZ"
    salary=9500
    bonus=500

    @property
    def totalsalary(self):
        return self.salary + self.bonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.bonus = val-self.salary

w=worker()
print(w.totalsalary)
w.totalsalary=11000
print(w.salary)
print(w.bonus)
