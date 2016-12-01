# you need to replace a section of a string with new comments.

str1 = "Here are a string"
# replaces 5 - 8 with "is"
corrected_str1 = str1[:5] + "is" + str1[8:]
print corrected_str1
