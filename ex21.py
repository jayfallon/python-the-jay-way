# -*- coding: utf-8 -*-

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

# a puzzle for the extra credit, type it in any way
print "here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that becomes: ", what, "can you do it by hand?"
