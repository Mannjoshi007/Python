#When we open a file in write mode it will erase the existing data of the file and replace the new one with it
a=open("demo.txt",'w')
a.write("This is the new content")
a.close()

#Writing various statements in the file
a=open("demo.txt",'w')
a.write("This")
a.write("is")
a.write("new one")
a.close()

#Writing various statements in the file with respect to new lines
a=open("demo.txt",'w')
a.write("This\n")
a.write("is\n")
a.write("new one\n")
a.close()