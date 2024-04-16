# This code is to show various fundamental concepts in Python, and has been created from modules that I have completed in 
# my Study with Whitecliffe.




# ************** Defining and setting type
# first_name = "Robert"
# last_name = "Paulson"
# print(first_name, last_name)




# ********************************* Numeric types ********************************************

# radius = 6
# pi = 3.1415926535897931
# area = pi * radius **2
#
# print(area)

# This code calculates the area of a circle given its radius.It performs arithmetic operations with integers and floats
# and works with complex numbers using pi times radius squared

# x = 4
# y = 7
# z = 34.7
# add = x + y + z
# print(add, type)

# x = 3 + 7j
# y = 9j
# imaginary_part_x = x.imag
# imaginary_part_y = y.imag
# print("imaginary_part of x:", imaginary_part_x)
# print("imaginary_part of y:", imaginary_part_y)



# *************************** String types **************************************************

# print(ord("G"))
# print(ord("l"))
# print(ord("e"))
# print(ord("n"))


# old = "God of nations"
# print(old)
# new = "God Defend New Zealand"
#
# # print(old.replace(old, new))
# print(old.replace(old, new).upper())

# God_of_nations = "text"
# text = "God Defend New Zealand"
# print(text.swapcase())

# quote from God of Nations
# quote = "God Defend New Zealand"
## print("Original quote:")
# print(quote)
## print("\nIn uppercase:")
# print(quote.upper())
#
# print("\nIn lowercase:")
# print(quote.lower())
#
# print("\nAs a title:")
# print(quote.title())
#
# print("\nWith a minor replacement:")
# print(quote.swapcase())
#
#
# input("\n\nPress the enter key to exit.")

# string manipulation functions like replace(), upper(), swapcase() and others
# I can replace parts of a string method to change the text to upper case, lower case or replace it entirely


# **************************** Boolean Types *************************************************
#  Boolean Values are only true or false

# Baby.py
#
# author: A. N. Other
# date: September 2016

# import random
#
# male = False
# male = bool(random.randint(0, 1))
#
# if (male):
#     print ("We will use name Rangi")
# else:
#     print ("We will use name Anihera")

# BoolTests.py
#
# author: A. N. Other
# date: September 2016

# print ("Test 1 ", bool(True))
# print ("Test 2 ", bool(False))
# print ("Test 3 ", bool("text"))
# print ("Test 4 ", bool(""))
# print ("Test 5 ", bool(" "))
# print ("Test 6 ", bool(0))
# print ("Test 7 ", bool())
# print ("Test 8 ", bool(3))
# print ("Test 9 ", bool(None))

# here I randomly assign a boolean value and print a message based on the boolean value.
# this shows how to use boolean values in conditionals.


# ******************************************* Casting *********************************************

# Casting.py
#
# @ author: A. N. Other
# date: September 2016

# variable set to integer
my_score = 201

print("The type of my_score is ", type(my_score),"\n")
print("my_score is ", my_score,"\n")

print("Casting to a string...\n")
# variable cast to string
my_score = str(my_score)

print("The type of my_score is now ", type(my_score),"\n")
print("my_score is ", my_score,"\n")

# defines a variable as an integer(my_score = 201) then casts it to a string and prints the changes in type (type(my_score))