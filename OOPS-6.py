class Workers:
    def name(self):
        print(f"ThE NAME of the worker is {self.na}.")
    def salary(self):
        print(f"The SALARY requirement of the worker {self.na} is {self.sal}.")

#Self parameter is used for giving the object name in the function directly.
#There happens replacement of the object self keyword by the object name when we have provided the self parameter.
#Self parameter is a compulsory command to be given while forming a function within classes.

Vishnu=Workers()
Vishnu.na='Vishnu'
Vishnu.sal=80000
Vishnu.name()
Vishnu.salary()

#We need to give evalue of the reqiured variable regarding the oject before calling the object.
#The value of the variable needs to be givn in the valid datatype format.