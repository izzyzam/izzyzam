Message = 'Whats your name? '
print(Message + " Izzy E is my name")
var = 1
account_balance = 1000.0
client_name = 'Izzy E'
print(var, account_balance, client_name)
#2.4 Python Variables
#using variables stores the results. for example, 'message = 'hello'' use print to print the stored variable or code in 'message'
#think it as boxes. You can call this box/container/variable any name as long as it has letters, digits, or _. Must begin with a letter, Upper and lower case matters, and dont use words that are keywords for Python. ie: cant call a variable 'import' since import is a keyword for Python
#you can put anything inside a variable!
print('Python version: ', + var)
#Rememeber you can you the + operator to output strings and variables like the example abouve
var = var +1
print(var)
#var was 1 but now var became 2, var is given a new value. It would be the same if we did the following:
var = 100
var = 200+300
print(var)
#var became a new value of 500 rather than 100.
a=4.0
b=9.0
c=(a + 4 + b -2) * 2
print(c)
john=3
mary=5
adam=6
total_apples=john+ mary + adam
print("Total number of apples: ", + total_apples)
sheep = 1
sheep += 1
print(sheep)