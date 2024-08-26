class Instrument:
    def __init__(self, size):
        self.size = size

class Stringed(Instrument):
    def __init__(self, n_strings):
        self.n_strings = n_strings

class Violin(Stringed):
    def __init__(self, cost):
        super().__init__(4)
        super(Stringed, self).__init__(50)
        self.cost = cost

my_violin = Violin(680)
print("size:", my_violin.size, 
      "\nstrings:", my_violin.n_strings, 
      "\ncost:", my_violin.cost)