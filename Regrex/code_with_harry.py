# in this file i am practising the regrex from the code with harry tutorial.
import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Indian no. : +919796623456
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haaaiaiinai'''

# Meta characters:-

# patt = re.compile(r'fass')
# patt = re.compile(r'.787')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'ai$')
# patt = re.compile(r'ha*')
# patt = re.compile(r'ha+')
# patt = re.compile(r'ha{3}')
# patt = re.compile(r'(ai){2}')
# patt = re.compile(r'ai|Fax')

# Special sequence:-
# patt = re.compile(r'\ATata')
# patt = re.compile(r'\bFax')
# patt = re.compile(r'mited\b')
# patt = re.compile(r'\d{5}-\d{4}') # search this 22209-1911
patt = re.compile(r'\b91979')

matches = patt.finditer(mystr)
for match in matches:
    print(match)