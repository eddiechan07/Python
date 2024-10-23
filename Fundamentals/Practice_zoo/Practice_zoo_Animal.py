class Animal:
    def __init__(self, name, age, health_lv, happiness_lv):
        self.name = name
        self.age = age
        self.health_lv = health_lv
        self.happiness_lv = happiness_lv
    
    def display_info(self):
        print(f"{self.name} : age = {self.age}, health = {self.health_lv}, happiness = {self.happiness_lv}")
        
    def feed(self, val=10):
        self.health_lv += val
        self.happiness_lv += val

