#The class in which inheritance is done is called child class.
#The class from which inheritance is made to be done is called as the parent class.
#Inheritance gets the complete control of the the parent class in the child class.
#There are multiple types of inheritance.

#A basic inheritance possessing program looks like:

class Company:
    Office = "abc"

    def salary(self):
        print(100000)

class Employeee(Company):
    language = "Python"

    def task(self):
        print("To do Programming.")

c=Company()
c.salary()
print(c.Office)
e=Employeee()
e.task()
e.salary()
print(e.language)
print(e.Office)
    
