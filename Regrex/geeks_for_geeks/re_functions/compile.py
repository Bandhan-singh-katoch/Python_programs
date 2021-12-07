# compile()
import re

str = "Aye, said Mr. Gibenson Stark"
patt = re.compile('[a-e]')     # class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
match = patt.findall(str)
print(match)

# output : ['e', 'a', 'd', 'b', 'e', 'a']