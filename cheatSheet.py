#when printing strings: you need quots but for numbers you dont need the quotes

print("Hello world!")
print(123+20)

#===================================================================================================================
# when declaring a variable: you just need to declare the name of the variable and give it a value

greeting = "Hello"
name = "Hamad"

#====================================================================================================================
#when concatenating 2 strings togeather it doesn`t require quotes

print(greeting + " " + name)

#=====================================================================================================================
# when you have 2 variables which are numbers like the example below when printing them it will do the math

value1 = 4
value2 = 10

print(value1+value2)

#=========================================================================================================================
# when you need to take an input from a user its just variable name and the input 

print("Please enter Your Name")
name2 = input()

print(greeting +" "+name2)

#===========================================================================================================================
#To take an input for number you have to say int

print("Please enter your Number")
number=int(input())
print(number)

# OR

#You can take input like:

number2 = int(input("Please enter your second number: "))
print(number + number2)

#==============================================================================================================================
# to print out an int and a string you need to format it E.g:

myName = "bob"
myAge = 20
#  print("My Name is "+myName+' '+ str(myAge)+" years old")

#Or

print("My name is {0} and my age is {1}".format(myName,myAge))

#==============================================================================================================================
# For loops

for i in range(0, 20):
    print("is is now {0}".format(i))

#============================================================================================================================
#Arrays

arr = [1,2,3,4,5,6] 

print(arr[-1])  #negative will always print out from the end of the array

#=============================================================================================================================
#If Statements

import random

number = random.randint(1,10)

tries = 1

print("I`m Thinking of a number between 1 and 10")

guess = int(input("Have a guess: "))

if guess > number:
    print("guess lower..........")
if guess <number:
    print("guess higher.........")
if guess == number:
    print("correct!!!!!!!!!!!")













