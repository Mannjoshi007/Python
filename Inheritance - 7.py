#This @classmethod decorator is used to make a method of the class its own attribute
class train:
    name="Rajdhani"

    @classmethod
    def changespeed(self,newspeed):
        self.speed=newspeed

t=train()
t.changespeed('250')
print(t.speed)
print(t.name)
print(train.speed)