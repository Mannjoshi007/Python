#File can be just read when made opened in the read mode, The file which is opened needs to be closed compulsarily
a=open("ME.txt","r")
b=a.read()
print(b)
a.close()


#Read mode is the by default one
a=open("ME.txt")
b=a.read()
print(b)
a.close()

#To read specified characters from a text file
a=open("ME.txt","r")
b=a.read(6)
print(b)
a.close()

#To Read lines of the particular file,We can make deifferent as well as the same variables for the mentioned task
a=open("ME.txt","r")
b=a.readline()
print(b)
b=a.readline()
print(b)
c=a.readline()
print(c)
d=a.readline()
print(d)
a.close()