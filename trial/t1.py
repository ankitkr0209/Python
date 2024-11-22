# class Animal:
#   def speak(self):
#     print("The animal makes a sound")
# class Dog(Animal):

#   def speak(self):
#     print("The dog barks woof!")

# dog = Dog()
# Animal.speak(dog) 

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("__WELCOME TO BCA LOTTERY ____________________________________________________")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

name = input("please enter your name ")
print("welcome back sir --------------- have a great day")
print("your account balance is $10,000")
print("lets start game") 


# Python code to demonstrate the Exception of 
# randrange(), ValueError, start >= start

import random

# Using randrange() to generate numbers from 500-100
# Raises Exception
#print ("Random number from 500-100 is : ",end="")
a= int(random.randrange(0,10))
if(a>4):
    result = "big"
else:
    result = "small"