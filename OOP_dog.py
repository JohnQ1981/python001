from io import BufferedReader


class Dog:
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
rain.perform_trick('jump on a loop')
rain.learn_trick('sit')
rain.learn_trick('sat')
rain.learn_trick('jump on a loop')
rain.perform_trick('jump on a loop')
print(rain.tricks)
print("*"*45)
print(type(otter))
print(isinstance(otter, Dog))
print("*"*45)
jules = Dog("Jules", "German Shepherd", 10003)
print("*"*45)
print(jules.name, jules.location, jules.breed)
print(jules.bark())
print("*"*45)
tine = Dog("Pumpkin", "France Sheppard", 64120)
print(tine.tricks, tine.bark())