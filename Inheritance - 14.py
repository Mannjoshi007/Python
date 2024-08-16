class editing:
    surname="Nothing"
    name="Anonymous"

    @property
    def The(self):
        return self.surname + self.name
    
    @The.setter
    def The(self,gi):
        return self.surname + self.gi
    
e=editing()
print(e.The)
e.name="Karan"
print(e.The)