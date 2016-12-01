def print_numbers(limit, adder):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + adder
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

limit = int(raw_input("Give me the limit number: "))
adder = int(raw_input("Give me the adder: "))
print_numbers(limit, adder)
