import re
from unittest import result

result = re.search(r"aza", "plaza")
print(result)
# print retorna ->  <re.Match object; span=(2, 5), match='aza'>
print(re.search(r"^x", "xenon"))
# print retorna -> <re.Match object; span=(0, 1), match='x'>
print(re.search(r"p.ng", "penguin"))
# print retorna -> <re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "Pangea", re.IGNORECASE))
# print retorna -> <re.Match object; span=(0, 4), match='Pang'>



#Questionar
#Fill in the code to check if the text passed contains the vowels
#a, e and i, with exactly one occurrence of any other character in between.
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True