# A module is a simply a Python file that contains code that can be re-used in other files.
#Modules allow us to break up complex programs into smaller, more manageable pieces across multiple files.
#Python comes with Built-In, Custom and 3rd Party Modules
from pickle import load
import calendar
import random as rand
#from math import *
from math import pi , sin, cos, tan
print(calendar.isleap(2021))
print(calendar.isleap(2022))
load.
print(calendar.weekday(2021,6,3))
ryear = rand.randint(1900,2022)
rmont = rand.randint(1,12)
rday = rand.randint(1,30)
day = calendar.weekday(ryear,rmont,rday)



print(pi)
print(sin(1))
if day == 0:
    print("It is Monday")
elif day == 1:
    print("It is a Tuesday")
elif day == 2:
    print("It is a Wednesday")
elif day == 3:
    print("It is a Thursday")
elif day == 4:
    print("It is a Friday")
elif day == 5:
    print("It is a Saturday")
elif day == 6:
    print("It is a Sunday")

print(sqrt(9))