#Class atttributes remain constant for the whole class and for any object of that class
#Attributes too are written in camelCase

class Employee:
    salary=370000
    company="XYZ"
    location="Work From Home"

John=Employee()
Karan=Employee()

print(John.company)
print(Karan.salary)

print(John.location)
print(Karan.company)

print(John.salary)
print(Karan.location)