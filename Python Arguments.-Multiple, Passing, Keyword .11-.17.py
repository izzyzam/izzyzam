print("The itsy bitsy spider" , "climbed up" , "the watersprout.")
#2.1.1.12 this print contains 3 arguments seperated by commas. Even though they are in separate "" the output will be a full sentence
print("My name is", "Python.")
print("Monty Python.")
#2.1.1.13 Positional way of passing arguments
#this means the first "string" will come first followed by the next "string" 
print()
print("My name is", "Python.", end= "Monty")
print("Monty Python.")
#2.1.1.14 Keyword arguments. These are special words change the behavior a bit.
#Keyword argument consist of three elements: a keyword, an equal sign, and a value assigned to the argument
#Keyword arguments have to be put after the last positional argument
#the argument "end" is followed by "=" and the value is " 'a space marker' "
#it seems like the end= " " took away the newline and merged the sentences together