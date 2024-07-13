#Seting Default Parameter gives an arguement to the function itself from the beginning
#This argument value is used in case of there is no providation of the argument for the function

def greet(name="Ayush"):
    print("Good Morning " + name) 

greet()

greet("Karan")