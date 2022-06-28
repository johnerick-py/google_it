import re

print(re.search(r"[Pp]ython", "Python"))
# saida: <re.Match object; span=(0, 6), match='Python'>
print(re.search(r"[a-z]", "The end of the highway"))
# saida: <re.Match object; span=(1, 2), match='h'>
print(re.search(r"[a-z]", "What a way to go"))
# saida: <re.Match object; span=(0, 1), match='w'>
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
# saida: <re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
# saida: <re.Match object; span=(0, 6), match='cloud9'>