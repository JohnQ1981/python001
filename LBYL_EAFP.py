#LBYL == Look Before You Leap 
#coding style where you explicitly test for pre-conditions before making calls or leaping.
#  Characterized by lots of if statements
#example
year = input("Enter a year: ")
if year.isnumeric():
    year = int(year) #<--- this is called leap, convert year to int once we know it is safe
else:
    year = "Not numeric"

print(year)

#EAFP = Easier to ask for forgiveness than permission
#"Assume things exist or will work, and catch exceptions if you are wrong"
#coding style characterized by lots of try/except blocks
try :
    year = int(input("Enter a year: "))
    
except ValueError:
    year = 2025
    print("That is not an int! ")

print(year)