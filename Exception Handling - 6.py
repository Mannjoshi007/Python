def bonus(num):

    try:
        return int(num) + 1 
    except:
        raise ValueError("You entered a wrong number.")

a=bonus(12)
print(a)

#Error will take place
b=bonus('hjf')
print(b)