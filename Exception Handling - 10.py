#We can even use try,else and finally altogether

num = input("Enter a number : ")
try:
    i=int(num)
    print(num)
except Exception as a:
    print('An error occured.')
    print(f"The error is {a}")
else:
    print("Done")
finally:
    print("You can leave")