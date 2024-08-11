#Operator overloading is useful for performance of arithmetic tasks when we do include operators in objects.
#This methods are known as the dunder methods.
#These methods help for the use of oprators in the class and objects.

class number:
    def __init__(self,n):
        self.nu=n

    def __mul__(self,nu2):
        print("The result will be printed.")
        return self.nu * nu2.nu

num1=number(2)
num2=number(3)
multi=num1*num2
print(multi)