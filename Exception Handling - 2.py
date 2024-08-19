try:
    n=int(input("Enter a number: "))
    c=1/n
    print(c)

except Exception as e:
    print("An error occured.")
    print(f"The error is {e}.")

print("Thank You.")
