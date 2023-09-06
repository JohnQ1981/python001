from random import randint
def form():
    f_n = input("Enter first name ")
    l_n = input("Enter last name ")
    if f_n.isalnum() and l_n.isalpha(): 
        return f_n , l_n
    else :
        raise ValueError("Invalid user name or chars in user name")


form()
 #try : <code>
 #except :<code>
try:
    num = int(input("enter a number "))
except ValueError:
    print(f"You entered non numeric so i will pick for you randomly")
    r = randint(0,15)
    num = r
    print(f"Random number is  {num}")
except EOFError:
    print("you did not enter any number so we will randomly pick one")
    r = randint(25,105)
    num = r
    print(f"Random number is  {num}")
print(f"You entered  {num}")

try :
    num = int(input("enter an integer "))
    print(10/num)
except ValueError:
    print("That is not an int! ")
except ZeroDivisionError:
    print("Cannot divide by zero!")