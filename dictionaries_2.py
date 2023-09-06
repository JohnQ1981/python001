prices = {
    'aragula': 1.10,
    'basil' : 2.54,
    "apples": 3.99,
    "blackberries": 4.99,
    'bananas': 0.59
}
product = input("enter what product are you buying? ")

if product in prices:
    price = prices[product]
    print(f" {product} are ${price} per lbs.")
else:
    print(f"{product} you entered is not in the list")


#using get() method
price = prices.get(product)
if price :
    print(f" {product} are ${price} per lbs.<---Using get() method")
else:
    print(f"{product} you entered is not in the list")