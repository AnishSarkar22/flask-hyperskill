class Animal:
    def __init__(self, species):
        self.species = species
        print("Animal __init__")


class Cat(Animal):
    def __init__(self, name):
        super().__init__("cat")
        self.name = name
        print("Cat __init__")

fluffy = Cat("Fluffy")
# Animal __init__
# Cat __init__

print(fluffy.species, fluffy.name)  # cat Fluffy
