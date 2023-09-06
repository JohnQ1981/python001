def average(*args):
    total = 0
    for c in args:
        total += c
    return total/len(args)

print(average(2,5,6,4,5,6,5,6,66,695,85.5,95.36,952.365,55,66,55,852.325,74))

def count_stuff(*args):
    print(f"You passed me {len(args)} arguments")

count_stuff(2,6,5,'l',6,'p')

def sums(*nums):
    total =0
    for c in nums:
       # if int(c.isdigit()):
            total += c
        #else:
         #   print("entered non numeric values")
    return total

print(sums(1,2,3,4,5))

def form(first_name,last_name,*others):
    
    print(f"Hi {first_name}, {last_name}, and {others}")

form(1,2,['s','h'])
#Given the following function:

def count(x,y,*args):
  return len(args)
#What does this function call return?

print(count(56, 99, True, "Chicken", 1))

#Given this (completely useless) function:

def silly_goose(num, *args):
  return args
#What does silly_goose return when we call silly_goose(1,2,3,4,5)
print(silly_goose(1,2,3,4,5))
