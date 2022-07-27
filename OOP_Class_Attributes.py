class Dog:
    species = "Dog Animals"
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
    
    def add_trick(self, new_trick):
        self.tricks.append(new_trick)
    
    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} does not know how to performs {trick}")

    def bark(self):
        print(f"{self.name} says WOOF!")

otter = Dog("Colt", "husky", 64063)
rain = Dog("Rain","Australian Shepherd", 98563)

p = otter.species
print(p)
r = rain.species
print(r)