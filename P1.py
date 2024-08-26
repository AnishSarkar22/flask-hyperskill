# 
class Drinks:
    pass

class PumpkinJuice(Drinks):
    pass

class Pastry:
    pass

class Sweets:
    pass

def find_the_parent(child):
    for base_class in Drinks, Pastry, Sweets:
        if issubclass(child, base_class):
            print(base_class.__name__)
            return
