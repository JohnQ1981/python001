user = ['Joe', 'Bucky', 42]
first, last , age =user
print(first)

# * unpacking
item = [4, "Pizza" , "Plain",16.98]
quantity, *others, price = item
print(others)
print(price)