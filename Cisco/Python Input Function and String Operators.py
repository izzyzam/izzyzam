# input() prompts the user to input data. you must assign the result to a variable! 
a = float(input("Enter any value: ")) #you are making a the variable and you are inserting whatever value insinde input
b = float(input("Enter any value: ")) #you must put float in front of input() to make sure it allows a float. Same with integer(input()) to insert integer

print(a + b) #you are using the input value, which is the a & b variable, and inserting it into print() 
print(b - a)
print(a * b)
print(a / b)

print("\nThat's all, folks!")

anything = input('Tell me anything...')
print('Hmm...', anything, '...Really')
#notice how input prompts you to insert a string, and it POPS out in the middle of your print()

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
#Adding float lets you do floats and note you can use two input() in a print()

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
#look at hypo. using the variables inside another variable but using the input() to create values and using operations to create the print info

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is ", + str((leg_a**2 + leg_b**2) ** .5))
#You can get rid of hypo and added the str() function.

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
#incorporating the lessons learned from print() adding the + to make it a sentence.

print("izzy" * 4)
#A string * a number or vice versa will produce the same string the amount the number is

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
#drawing a simple rectangle! see how you're using the number * string to create the top and bottom while also creating the space inside.

x = float(input("Enter value for x: "))

y = (1/(x+1/(x+1/(x+1/(x))))) # Write your code here.
#Rememeber the order of operations when conducting this. Use paranthesis smartly. It took me 10 to figure how to correctly set it up.
print("y = ", y )
#Try it out with 1, 10, 100, -5