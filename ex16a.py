# --*-- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to open %r." % filename
print "Opening file..."
target = open(filename, "r")

print target.read()

target.close()
