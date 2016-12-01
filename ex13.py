# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv

print "What kind of animal are you?"
animal = raw_input()

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "You are a %s" % animal
