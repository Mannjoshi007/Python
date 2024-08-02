#Single Level Inheritance means the child class gets inherited of from one parent class only
class Company:
    name="XYZ"

class Worker(Company):
    location="Work From Home"

c=Company()
w=Worker()
print(w.location)
print(w.name)