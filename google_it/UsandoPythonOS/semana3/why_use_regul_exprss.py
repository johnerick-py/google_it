import re
from unittest import result

from pyparsing import Regex

log = "July 31 07:51:48 mycomputer bad_process[12345]: Error performing package upgrede"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])