#This method is useful to get the length of the object.
#But we will always be resulted with the output which has been metioned in the method declaration.

class num:

    def __init__(self,n):
        self.n=n

    def __len__(self):
        return 1

Number=num(5)
print(len(Number))