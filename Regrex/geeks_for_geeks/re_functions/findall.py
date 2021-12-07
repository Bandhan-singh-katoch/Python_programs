# re.findall() : return all non overlapping matches of pattern in a string as a list of string
# program to find digits
import re

str = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
match = re.findall('\d+',str)
print(match)