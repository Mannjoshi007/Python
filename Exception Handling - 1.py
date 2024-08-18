#Exception means the error which gets raised due to some malfunction in the code or the invalid input provided.

while(True):
    print("Press Q to quit the program.")
    num=input("Enter a random number : ")
    if num=='Q':
        break

    try:
        print("Processing")
        num=int(num)
        if num<10:
            print("You have entered a number lesser than 10.")
        else:
            print("You have given an appropriate input.")

    except Exception as f:
        print(f"Your input is inappropriate.\nThe error which occured is {f}.")

print("You are done!")




