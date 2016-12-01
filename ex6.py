# -*- coding: utf-8 -*-
# sets the value of x where an integer is inserted
x = "There are %d types of people." % 10
# sets the value of binary
binary = "binary"
# sets the value of do_not
do_not = "don't"
# sets the value of y where two strings are inserted
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x and y
print x
print y

# prints where x is inserted as a string
print "I have said: %r" % x
# prints where y is inserted as a string
print "I also said: '%s'." % y

# sets value of hilarious
hilarious = False
# sets value of joke_evaluation with evaluator?
joke_evaluation = "Isn't that joke so funny?! %r"
# prints the evaluation of the joke against hilarious
print joke_evaluation % hilarious

# sets the values of w and e
w = "This is the left side of..."
e = "a string with a right side."

# prints w + e
print w + e
