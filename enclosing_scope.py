def outer():
    animal = "lion"
    def inner():
        print("Inside inner func: ", animal)
    inner()
outer()
#built in scopes are available anywhere

num = 333
str(num)
print(str(num))
#LEGB = Local, Enclosing,Global and BuiltIn Scopes

