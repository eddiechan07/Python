from Practice_zoo_Animal import Animal

class Lions(Animal):
    
    def __init__(self, name, age, health_lv = 80, happiness_lv = 80, leadership_point = 100):
        super().__init__(name, age, health_lv, happiness_lv)
        self.leadership_point = leadership_point
    
    def feed(self, val=10):
        self.health_lv += val
        self.happiness_lv += val