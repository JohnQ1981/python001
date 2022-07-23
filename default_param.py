def greet(msg, person):
    print(f"{msg},{person}")

greet("Hi", "John")
# Default value should come after required parameter

def greet(person, msg="Hi"):
    print(f"{msg},{person}")
greet("Tanya")

def greet(person="stranger", msg="Hi"):
    print(f"{msg},{person}")

greet()
