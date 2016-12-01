# -*- coding: utf-8 -*-
name = 'Zed A Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # lb
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilo = 0.453592
cent = 2.54

print "Let's talk about %r." % name
print "He's %d inches tall" % height
print "That's %d in centimeters." % (height * cent)
print "He's %d pounds heavy." % weight
print "That's %d in kilos." % (weight * kilo)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
