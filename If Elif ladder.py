a=int(input("Enter a number "))
b=int(input("Enter another number: "))
num=b
def sum(num):
    return num+a

g=sum(b)

if(g>50):
    print("The value exceeds allowed capacity")
elif(g<50):
    print("The value is within allowed capacity")
elif(g=50):
    print("You entered the perfect value!")