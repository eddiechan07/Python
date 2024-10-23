from Practice_zoo_Animal import Animal

class Tigers(Animal):
    
    def __init__(self, name, age, health_lv = 50, happiness_lv = 80 , attack_point = 100):
        super().__init__(name, age, health_lv, happiness_lv)
        self.attack_point = attack_point
    
    def feed(self, val=25):
        self.health_lv += val
        self.happiness_lv += val
        return self
    
    def display_info(self):
        super().display_info()