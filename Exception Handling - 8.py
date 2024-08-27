#We can even use the try block with else.
#The code within else will only be executed if the try block remains true.

num = input("Enter a number : ")
try:
    i=int(num)
    print(num)
except Exception as a:
    print('An error occured.')
    print(f"The error is {a}")
else:print("Done!!")