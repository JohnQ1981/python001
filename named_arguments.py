#also called keyword argument
def get_total(price, qty=1, tax=0.02, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal *(1+tax))

get_total(4.99, 5, 0.015, 0.2)

get_total(9.75, 5, 0.01, 0.5)
get_total(price=9.75, qty=3,tax=0.03,discount=0.5)
get_total(qty=5, price=5,discount=0.5,tax=0.03)
get_total(price=5, qty=5,discount=0.5,tax=0.03)
get_total(9.99)
get_total(5.99, discount=.25)