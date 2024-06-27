Dictionary1={
    "Word":"The combination of letters" ,
    "Sentence":"the comination of words",
    12:"A number",
    1.265: "A decimal number"
}


#To print all the keys of the dictionary
print(list(Dictionary1.keys()))

#To print all the values of the dictionary
print(list(Dictionary1.values()))

#To print all the items of the dictionary, item means a key - value pair
print(list(Dictionary1.items()))

#To add some data in the existing dictionary
new={True:"A boolean value"}
Dictionary1.update(new)
print(Dictionary1)

#To get the value of the mentioned key
print(Dictionary1.get(True))