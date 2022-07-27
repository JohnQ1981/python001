#Inheritance is the same as in Java,basically you want to have common things in one class and 
# have other classes to inherit those methods
#Example of Cat, all Cats do meows,so meowing can be in parent class
# where other classes can inherit. or walking, etc...
#the idea is the same as in Java
class Cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name} meows")

class Lion(Cat):
    def roar(self):
        print(f"{self.name} roars")

class Cougar(Cat):
    def __init__(self, name, pride_name):
        super().__init__(name)
        self.pride_name = pride_name
    def purr(self):
        print(f"{self.name} purrs")

liongking = Lion("Simba")
liongking.meow()
liongking.roar()

puma = Cougar("Puma", "Awesome")
puma.purr()
puma.meow()
print(f"{puma.pride_name} is Pride name of {puma.name}")
