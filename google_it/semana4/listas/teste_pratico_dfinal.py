# Pergunta 1
# Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill
# in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

# filenames = ["program.c", "stdio.hpp",
#              "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# newfilenames = []
# for filename in filenames:
#     newfilenames.append(filename)
#     if ".hpp" in filename:
#         var = " ".join(newfilenames)
#         var = var.replace(".hpp", ".h")
#         var = var.split()
#         newfilenames.clear()
#         newfilenames.extend(var)


# using as many lines of code as your chosen method requires.

# print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# 2.
# Pergunta 2
# Let's create a function that turns text into pig latin:
# a simple text transformation that modifies each word moving the first character to the end
# and appending "ay" to the end. For example, python ends up as ythonpay.

# def pig_latin(text):
#   words = text.split()
#   pigged_text = []

#   for word in words:
#     word = word[1:] + word[0] + 'ay'
#     pigged_text.append(word)

#   return ' '.join(pigged_text)

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# 3.
# Pergunta 3
# The permissions of a file in a Linux system are split into three sets of three permissions: read,
# write, and execute for the owner, group, and others. Each of the three values can be expressed as an
# octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute.
# Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#  For example:
#  640 is read/write for the owner, read for the group,
#  and no permissions for the others; converted to a string, it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others;
#  converted to a string, it would be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.


# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4,"r"),(2,"w"),(1,"x")]
#     #Iterating over each digit in octal
#     for digit in [int(n) for n in str(octal)]:

#         #Checking for each of permission values
#         for value, letter in value_letters:
#             if digit >= value:
#                 result += letter
#                 digit -= value
#             else:
#                 result += "-"
#     return result

# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------

# 5.
# Pergunta 5
# The group_list function accepts a group name and a list of members,
# and returns a string with the format: group_name: member1, member2, …
# For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

# def group_list(group, users):
#   members = ", ".join(users)
#   return "{}: {}".format(group, members)

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"

# Pergunta 6
# The guest_list function reads in a list of tuples with the name,
# age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __."
# for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer"))
# should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25
# years old and works as Engineer. Fill in the gaps in this function to do that.

# def guest_list(guests):
#     ken = guests[0][0]
#     k_year = guests[0][1]
#     k_work = guests[0][-1]
#     pat = guests[1][0]
#     p_year = guests[1][1]
#     p_work = guests[1][-1]
#     aman = guests[-1][0]
#     aman_year = guests[-1][1]
#     aman_work = guests[-1][-1]
        

#     print(
# """
# Output should match:
# {} is {} years old and works as {}
# {} is {} years old and works as {}
# {} is {} years old and works as {}
# """.format(ken, k_year, k_work, pat, p_year, p_work, aman, aman_year, aman_work))


# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
#             ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
