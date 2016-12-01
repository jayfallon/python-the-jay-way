# you want to compare strings to see if two strings have the same value or checking to see whether two names point to the same object.

str1 = "Hello"
str2 = "Hello"

if str1 == str2:
    print("The strings match")
else:
    print("The strings are not equal")

from sys import argv

script, arg1, arg2 = argv

if arg1 == arg2:
    print "The terms are equal"
else:
    print "The terms are not equal"    
