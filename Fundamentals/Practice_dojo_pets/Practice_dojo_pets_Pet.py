class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name , type , tricks, energy, health):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleep. Energy increased to {self.energy}")
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating. Energy increased to {self.energy} and health increased to {self.health}")
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name} is playing. Health increased to {self.health}")
        return self
    # noise() - prints out the pet's sound
    def noise(self, sound):
        print(f"{self.name} is making a sound: '{sound}'")
        
class Dog(Pet):
    def __init__(self, name , type , tricks, energy, health):
        super().__init__(name , type , tricks, energy, health)
    def noise(self):
        print(f"{self.name} barks: Woof Woof!")
        
class Cat(Pet):
    def __init__(self, name , type , tricks, energy, health):
        super().__init__(name , type , tricks, energy, health)
    def noise(self):
        print(f"{self.name} barks: Miao Miao!")
        
