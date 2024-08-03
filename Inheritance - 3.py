#When we inherit  a new class with reference to two or more existing classes the inheritance is kniwn as multi-level inheritance 
#We can have same attribute and methods in different classes, if wwe create the same in a single class ther the later one does overwrite the former

class Freelancer:
    company="XYZ"

class Employee:
    salary=120000
    company="ABC"

#When we have same attribute or methods in different classes, the value are expected as per the former class name while inheriting
#1st possibility

class Worker(Freelancer,Employee):
    name="Karan"

w=Worker()
print(w.salary)
print(w.company)
print(w.name)

class Worker(Employee,Freelancer):
    name="Karan"

w=Worker()
print(w.salary)
print(w.company)
print(w.name)
