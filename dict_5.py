prices = {
    'aragula': 1.10,
    'basil' : 2.54,
    "apples": 3.99,
    "blackberries": 4.99,
    'bananas': 0.59
}
for c in prices:
    print(f'{c} are ${prices[c]} per lbs.')

print(prices.items())
print("Above are Items ", '*'*40)
print(prices.keys())
print("Above are keys ", '*'*40)
print(prices.values())
print("Above are Values ", '*'*40)

list_of_keys = list(prices.keys())
print(list_of_keys)