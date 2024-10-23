from Practice_zoo_Animal import Animal

class Bears(Animal):
    
    def __init__(self, name, age, health_lv = 80, happiness_lv = 50, defence_point = 100):
        super().__init__(name, age, health_lv, happiness_lv)
        self.defence_point = defence_point
    
    def feed(self, val=20):
        self.health_lv += val
        self.happiness_lv += val