order = {"cost": 3.5, "quantity": 12}
order.update({"product":'taco' , 'date': '03/14/2019'}) #using update() method
print(order)
for c, b in order.items():
    print(c, b)
# ** is used to combine multiple dictionaries into a new resulting dictionary
dict1 = {'a': 1, 'b': 2, 'Color': 'black'}
dict2 = {'c': 3, 'd': 4, 'Color': 'white'}
dict5 = {'color': 'Blue'}
dict3 = {**dict1, **dict2}
print(dict3)
# new operator for dict union
dict4 = dict3 | dict2 | dict5
print(dict4)