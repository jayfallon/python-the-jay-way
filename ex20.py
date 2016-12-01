# -*- coding: utf-8 -*-

# import argv module from sys
from sys import argv

# declare arguments
script, input_file = argv

# define the print_all function to take one argument
def print_all(f):
    # print the contents of that file
    print f.read()

# define the rewind argument
def rewind(f):
    # use the seek function to find the start of the file
    f.seek(0)

# define the print one line function
def print_a_line(line_count, f):
    # print the line number followed by the line contents
    print line_count, f.readline()

# define the current_file variable with the input file argument
current_file = open(input_file)

print "First let's print the whole file:\n"
# print the content of the entire file
print_all(current_file)

print "Now let's rewind kind of like tape"
# rewind to the beginning of the current file
rewind(current_file)

print "Let's print three lines"
# set the current line to be the first line in the file
current_line = 1 # line 1
# print the first line of the current file
print_a_line(current_line, current_file)

# set the current_line to be one after the previous
current_line += 1 # line 2
# print that line
print_a_line(current_line, current_file)

# set the current_line to be one after the previous
current_line += 1 # line 3
# print that line
print_a_line(current_line, current_file)

current_file.close()
