# sets the value of people, cars and trucks variables
people = 29
cars = 10
trucks = 152

# if the number of cars is greater than the number of people, print message 1.
if cars > people:
    print "We should take the cars."
# else if the number of cars is lesser than the number of people, print message 2.
elif cars < people:
    print "We should not take the cars."
# if the number of cars is neither greater nor lesser than the number of people, print message 3.
else:
    print "We can't decide."


if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay at home."
