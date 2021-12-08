#In-built Functions

#int()
#input()
#str()
#bool()

#Module Functions

import math
print(dir(math))

from math import sqrt #from math is used to get a single functions from math module
from math import * #* is used to get all functions
print(sqrt(16))
print(sqrt(400))

#User Defines Functions
def add(firstnum, secondnum):
#def add(firstnum, secondnum = 4): This is used as a default input if user didnt defined the second number
    print(firstnum + secondnum)
add(1, 2)
