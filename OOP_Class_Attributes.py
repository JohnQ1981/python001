class Dog:
    species = "Dog Animals" #Class Attribute is like a Static variable in Java, Moon in the Sky.
    num_dogs = 0
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs += 1
    
    @classmethod
    def register_stray(cls):
        return cls("coming soon",'unknown',45444)

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

un = Dog.register_stray()
print(un.name, un.location)
print(un.bark())
otter = Dog("Colt", "husky", 64063)
rain = Dog("Rain","Australian Shepherd", 98563)
pumpkin = Dog("Pumpkin", "Bulldog",64034)
p = otter.species
print(p)
r = rain.species
print(r)
print(Dog.species)
Dog.species = "Canine"
p = otter.species
print(p)
r = rain.species
print(r)
print(Dog.species)
print(Dog.num_dogs)