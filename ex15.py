# -*- coding: utf-8 -*-

# imports the argv module from sys
from sys import argv

# defines the initial variables required to run the script
script, filename = argv

# opens the file named in the filename variable
txt = open(filename)

# prints thename of filename
print "Here's your file %r:" % filename
# prints the contents of filename
print txt.read()

# prints a prompt for the name of the file again
print "Type the filename again:"
# records the name of the file
file_again = raw_input("> ")

# creates a variable that will call for filename to be opened
txt_again = open(file_again)

# prints the contents of the filename again.
print txt_again.read()
