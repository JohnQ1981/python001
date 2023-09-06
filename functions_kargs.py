# **kwargs we can use the ** notation to write functions that accept any number of keyword arguments
def demo(**kwargs):
    print(kwargs)

demo(color ="red", age =12)
print(type(demo))

def laugh(**stuff):
  return True

laugh(age =25, amount =3)
print(type(laugh(age =25, amount =3)))