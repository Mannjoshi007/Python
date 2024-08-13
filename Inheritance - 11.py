#This dunder method is useful in the case of printing of an object directly from our side.
#There happes avoidal of the error to be get printed.
#It will have us the content provided in the output.

class num:
    
    def __init__(self,n):
        self.n=n


    def __str__(self):
        return f"The number is {self.n}"


Number=num(5)
print(Number)