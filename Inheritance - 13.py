#The use of len() function to get the length of the object.

class vec:
    def __init__(self,ve):
        self.v=ve

    def __len__(self):
        return len(self.v)

V1=vec([2,6,5,6,1])
print(len(V1))
V2=vec([5,6,4,89,899665,544,6416])
print(len(V2))
