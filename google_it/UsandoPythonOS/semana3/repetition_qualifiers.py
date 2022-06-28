from cgi import print_arguments
import re

print(re.search(r"Py.*n", "Pygmallion"))
# <re.Match object; span=(0, 10), match='Pygmallion'>
print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'>
print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+", "boil"))
# None

#questionary
#The repeating_letter_a function checks if the text passed includes the
#letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana")
#is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work.

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


#-------------------------------------------------------------------------

print(re.search(r"p?each", "To each their own"))
# <re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "i like peaches"))
# <re.Match object; span=(7, 12), match='peach'>