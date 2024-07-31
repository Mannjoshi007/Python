class Employee:
    company="ABC"
    Salary=960000
    name="Akash"
    

    def __init__(self):
        print(f"Hello {self.name}, Welcome!")

Akash=Employee()


class Workers:
    def __init__(self,name):
        self.name=name
        print("Worker entry has been made.")

    def details(self):
        print(f"The name of the new worker is {self.name}.")

Ketul=Workers('Ketul')
Ketul.details()
