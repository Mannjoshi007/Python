#Instance attributes make the value of the class attributes different for the paricular considered object
#This do not cause any difference in the original value of the class attribute, it will remain the same only for the other relating objects

class Employee:
    salary=370000
    company="XYZ"
    location="Work From Home"

John=Employee()
Karan=Employee()

John.company="ABC"
Karan.location="Office"
print(John.company)
print(Karan.company)
print(John.salary)
print(Karan.location)
print(John.location)