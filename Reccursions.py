#Recurrsions are used where ther happens recoccurence of th function in the function itself

def  Factorial(n):
    if n==1 or n==0:
        return 1
    return n*Factorial(n-1)

f=Factorial(4)
print(f)