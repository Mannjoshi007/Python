#Constrctor gets executed directly only by the creation of an object.
#It do not require to be called.
#It is a self calling method..

class Employee:
    company="ZXC"

    def __init__(self):
        print("Welcome! The object has been created.")

rahul=Employee()

    