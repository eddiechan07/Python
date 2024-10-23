from Practice_dojo_pets_Pet import Dog

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"{self.first_name} is waliking with {self.pet.name}")
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name} with {self.pet_food}")
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}")
        self.pet.noise()
        return self

# Create an instance of Pet
Tanso = Dog("Tanso", "Golden Retriever", "rolling", 50, 100)
# Create an instance of Ninja with Tanso as the pet   
Shinobi = Ninja("Shinobi", "Lucas", "bell", "candybar", Tanso)

Shinobi.walk().feed().bathe()