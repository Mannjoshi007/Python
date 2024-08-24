try:
    n=int(input("Enter a number: "))
    c=1/n
    print(c)

except ZeroDivisionError as e:
    print("An error occured.")
    print(f"The error is {e}.")
    print("Do not enter zero.")

print("Thank You.")
