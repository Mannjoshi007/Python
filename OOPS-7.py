#When we declare a function(method) as static method there is no need of any data input from the object creted for the function.
#There remains no connection of the function with the object created.

class Welcome:

    @staticmethod
    def greet():
        print("Good Morning ,Welcome! Boss. ")

Preet=Welcome()
Preet.greet()
