#The statement in finally will be executed in cases of failure or performance of the try block.

num = input("Enter a number : ")
try:
    i=int(num)
    print(num)
except Exception as a:
    print('An error occured.')
    print(f"The error is {a}")
finally:
    print("Completed")
