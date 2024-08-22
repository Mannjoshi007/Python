try:
    n=int(input("Enter a number: "))
    c=1/n
    print(c)

except ValueError as e:
    print("An error occured.")
    print(f"The error is {e}.")
    print("Please enter a valid value.")

print("Thank You.")
