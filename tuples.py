# tuples are kind of lists but immutable, they cannot be changed once created
# tuples like lists are ordered and indexed collections
# unlike Lists, they are immutable. REMEMBER LISTS ARE MUTABLE IN PYTHON
dishes = ("burrito", "taco","fajita","meat", True, False , ['a,b,c,d' ,5 ,6],True, True)
for c in dishes:
    print(c)

first_tuple = (3,)
print(first_tuple)
print(dishes[3])
print(dishes[3:6])
print(dishes.index(False))
print(dishes.count(True))

dishes[6].append("haha")
print(dishes)