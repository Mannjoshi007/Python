#We can directly open a file by the use of with statement

with open('demo.txt') as f:
    g=f.read()
print(g)

with open('demo.txt','w') as a:
    f=a.write("Hi")
#The following line will give the number of characters that have been added to the new file 
print(f)

#While using with statement we do not need to close the file
#The operation on file happens by openning the file on a variable name's basis