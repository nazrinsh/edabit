import re
pattern = "red flag|blue flag"


import re

txt1 = "red flag blue flag"

txt2 = "yellow flag red flag blue flag green flag"

txt3 = "pink flag red flag black flag blue flag green flag red flag"

print(re.findall("red flag|blue flag", txt1))
#output: ['red flag', 'blue flag']
print(re.findall("red flag|blue flag", txt2))
#output: ['red flag', 'blue flag']
print(re.findall("red flag|blue flag", txt3))
#output: ['red flag', 'blue flag', 'red flag']

