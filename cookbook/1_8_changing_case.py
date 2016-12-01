# you need to set the case of the characters either all uppercase or all lowercase

str1 = "Hello World"
print(str1.lower())
print(str1.upper())

print(str1.center(40," "))

str2 = "This apparition will vanish."
sub = "i"
print str2.count(sub)
print str2

str3 = "This is a marvellous string"
str4 = str3.encode('base64', 'strict')
print str4
print "Decoded string: " + str4.decode('base64', 'strict')

suffix = "vanish."
print str2.endswith(suffix)

str5 = "You might like\t to read this."
print str5
print str5.expandtabs()
print str5.expandtabs(32)

str6 = "This is very important."
str7 = "very"
print str6.find(str7)

str8 = "This is the greatest string of all time."
str9 = "string"
print str8.index(str9)
print str8.index(str9, 10)
print str8.index(str9, 10)

str10 = " "
print str10.isspace()

str11 = "Hey now brown cow."
print str11.istitle()
str12 = "Hey Now Brown Cow"
print str12.istitle()
