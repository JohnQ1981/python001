def zoo():
    animal = "dolphin"
    print("Inside Zoo Function:", animal)

zoo()
#since animal is in local cope
#below print will not work
#print(animal) #<<<< will not work
# variables inside the loops or if conditions are global in scope

for char in "Octopus":
    print(char)
    color = "magenta"

print("After Loop ", color)

if color == "magenta":
    color2 = "red"

print("Variable inside the if: ", color2)