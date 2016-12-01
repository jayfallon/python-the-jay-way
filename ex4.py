# assigns cars the value of 100
cars = 100
# number of spaces per car
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# calculates numbers of cars that don't have drivers
cars_not_driven = cars - drivers
# calculates number of cars that have drivers
cars_driven = drivers
# calculates total car capacity for passengers
carpool_capacity = cars_driven * space_in_a_car
# calculates average passenger per car
average_passenger_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We be to put about", average_passenger_per_car, "in each car."
