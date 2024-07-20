#When we open a file in append mode it will update the existing comtent of the file with the mentioned one
a=open("demo.txt",'a')
a.write("This is the new content")
a.close()

#Appending various statements in the file
a=open("demo.txt",'a')
a.write("This")
a.write("is")
a.write("new one")
a.close()

#Appending a statement in the existing file
g=open("demo.txt",'a')
g.write("The\n")
g.close()

#Appending various statements in the file with respect to new lines
a=open("demo.txt",'a')
a.write("This\n")
a.write("is\n")
a.write("new one\n")
a.close()