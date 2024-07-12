#Arguments in a function describe the type of content on which the fuction will be acting 
#Arguments store the given value in as variables and thus, are used for further applications within a function itself

Employee=input("Entter your name, please ")

def greet(name):
    print("Hello! Good Morning,",name)

working=greet(Employee)


def sum(n1,n2):
    return n1+n2

Total=sum(4,6)
print(Total)