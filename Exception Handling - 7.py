#Try block is always made to be used with except block

num = input("Enter a number : ")
try:
    i=int(num)
    print(num)
except Exception as a:
    print('An error occured.')
    print(f"The error is {a}")