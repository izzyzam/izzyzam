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
#with the += component is a shortcut way to not continuously do sheep = sheep + 1. Can do it with x = x*2 as x *= 2.
kilometers = 12.25
miles = 7.38

miles_to_kilometers = (miles * 1.61)
kilometers_to_miles = (kilometers / 1.61)

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#with with Lab, we converted km to miles and miles to km. Each mile has 1.61 km.
x = -1
x = float(x)
y = (3*x**3 - 2*x**2 + 3*x - 1)
print("y =", y)
#this Lab had me taking the expression 3x3 - 2x2 + 3x - 1 and making it compatiable and having it = to the value of y. i added parathesis and the * to make it work. Note that it has x = float(x) to give y = a float answer
a = 6
b = 3
a /= 2 * b
print(a)
#print 2*b=6 a=6-> 6/6=1.0
