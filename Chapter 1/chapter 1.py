#This program says hello and asks for a name and age
#print function to print a string
print('Hello, world!')
print('What is your name?')
#declaring a string type variable and using input function for user inputs
myName = input()
#string concatenation to combine two strings
print('It is good to meet you, ' + myName)
print('The length of your name is')
#len() function to find the character length of a string
print(len(myName))
print('What is your age?')
myAge = input()
#int function to convert a string to int
#then adding 1 to the converted int
#then converting new total back to a string
#lastly string concatenation to combine the 3 strings
print('You will be ' + str(int(myAge) + 1) + ' in a year')