def numbers(limit, plus):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is: %d" % i
        numbers.append(i)
        i = i + plus
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

user_limit = int(raw_input("Give me a limit "))
user_plus = int(raw_input("Give me a plus "))
numbers(user_limit, user_plus)




# def regnal(top):
#     print "Your number is: %d" % top
    # i = 0
    # numbers = []
    # while i < top:
    #     print "At the top i is %d" % i
        # numbers.append(i)
        #
        # i = i + 1
        # print "Numbers now: ", numbers
        # print "At the bottom i is %d" % i

# regnal(top)

# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
# print "The numbers: "
#
# for num in numbers:
#     print num
