# SETS are unordered Collections with no duplicate elements
# Only immutable elements!
#No Order
#sets are created as follow:
evens = {2,4,6,8,10,12,14}

for k in evens:
    print(k)

evens.add(20)
evens.add(25)
print(evens)
evens.remove(25)
#discard() is like a remove() but will not throw error for missing value
evens.discard(44)
print(evens)
evens.clear()
print(evens)