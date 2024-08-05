#In above uploaded programs the word multiple ha been mistakenly written as multi-level
#Multi-level inheritance means inheriting in a flow step-wise process
#It means that the child class of a parent class will become the parent class of the new child class
#It is like the flow of generations

class breath:
    say="Breathing"

class walk(breath):
    suggest="Walking and Breathing"

class learn(walk):
    tell="Learning along with walking while walking"

b=breath()
w=walk()
l=learn()
print(b.say)
print(w.say)
print(w.suggest)
print(l.say)
print(l.suggest)
print(l.tell)

