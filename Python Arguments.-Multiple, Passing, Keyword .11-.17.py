print("The itsy bitsy spider" , "climbed up" , "the watersprout. \n")
#2.1.1.12 this print contains 3 arguments seperated by commas. Even though they are in separate "" the output will be a full sentence
print("My name is", "Python.")
print("Monty Python.")
#2.1.1.13 Positional way of passing arguments
#this means the first "string" will come first followed by the next "string" 
print()
print("My name is", "Python.", end= " ")
print("Monty Python.")
#2.1.1.14 Keyword arguments. These are special words change the behavior a bit.
#Keyword argument consist of three elements: a keyword, an equal sign, and a value assigned to the argument
#Keyword arguments have to be put after the last positional argument
#the argument "end" is followed by "=" and the value is " 'a space marker' "
#End= " " ends the the print() with a space and if there is a following print() it will continue with that one.
print('My name is', end=' what? My name is who? Chka chka ')
print('Monty Python.')
#continue .14 Another example of end= but with string. You can add whatver value you wish to it.
print('My', 'name', 'is', 'Monty', 'Python.', sep='=')
print('My', 'name', 'is', 'Monty', 'Python.', sep='-')
print('My', 'name', 'is', 'Monty', 'Python.', sep='      ')
#2.1.1.16 Keyword arguments
#Sep is another keyword argument. It seperates the strings print() with whatever value. It can be a -, =, any number of spaces, etc
print('My', 'name', 'is', sep='-', end='*')
print('Monty', 'Python.', sep='*')
print('My', 'name', 'is', sep='-', end='2*')
print('Monty', 'Python.', sep='*', end='4*\n')
print("Programming","Essentials","in", sep='**', end='...')
print("Python")
#continue .17 & .18 LAB using both sep and end keyword arguments with a different value in them