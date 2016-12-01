# -*- coding: utf-8 -*-

# we define the function and the name of the arguments it takes
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # we print out the # of cheeses given for each print req below
    print "You have %d cheeses!" % cheese_count
    # we print out the # of crackers from each print req below
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# we assign the arguments of the cheese_and_crackers function, and that in turn prints them
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# we assign values to two new variables
amount_of_cheese = 10
amount_of_crackers = 50
# we pass those variables as arguments to our function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# we do math as the arguments
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# we combine variables and math as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def jays_function(number_of_sodas, number_of_waters, number_of_cokes):
    print "You have %d sodas." % number_of_sodas
    print "You have %d waters." % number_of_waters
    print "You have %d cokes." % number_of_cokes
    print "Time to order more.\n"

jays_function(12, 4, 8)
amount_of_sodas = 16
amount_of_waters = 20
amount_of_cokes = 4
jays_function(amount_of_sodas, amount_of_waters, amount_of_cokes)
jays_function(10 + 3, 2 - 1, 11 + 100)
jays_function(amount_of_sodas + 21, amount_of_waters + 30, amount_of_cokes - 2)
