from Practice_zoo_Tigers import Tigers
from Practice_zoo_Bears import Bears
from Practice_zoo_Lions import Lions

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
    def add_lion(self, name, age):
        self.animals.append(Lions(name, age))
        return self
    
    def add_tiger(self, name, age):
        self.animals.append(Tigers(name, age))
        return self
    
    def add_bear(self, name, age):
        self.animals.append(Bears(name, age))
        return self
    
    def print_all_info(self):
        print("-"*10, self.zoo_name,"-"*10 )
        for animal in self.animals:
            animal.display_info()


zoo = Zoo ("Yao's Zoo World")
zoo.add_tiger("Cindy", 26).add_tiger("Windy", 16).add_tiger("Kindy", 30)
zoo.add_lion("Bleeder", 19).add_lion("Berrt", 20).add_lion("Luffy", 16)
zoo.add_bear("Winne", 20).add_bear("Lucas", 23).add_bear("King", 24)

# cindy.display_info()
zoo.print_all_info()