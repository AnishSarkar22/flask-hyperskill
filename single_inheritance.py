# parent class
class Animal:
    def __init__(self, name):
        self.name = name

# child class
class Dog(Animal):
    pass

cow = Animal("Bessie")  # instance of Animal
corgi = Dog("Baxter")   # instance of Dog