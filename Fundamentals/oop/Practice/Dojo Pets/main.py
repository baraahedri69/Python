class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        print(f"This is Ninja information {self.first_name} {self.last_name} with {self.treats} and {self.pet_food}")
        
        
    def walks(self):
        print(f"{self.first_name} walks their pet.")
        self.pet.play()

    def feeds(self):
        print(f"{self.first_name} baths their pet.")
        self.pet.eats()

    def bathe(self):
        print(f"{self.first_name} baths their pet.")
        self.pet.noise()

class Pet:

    def __init__(self, name , type , tricks, energy= 100, health= 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
        print(f"This is our pet information: {self.name}, type: {self.type} and tricks: {self.tricks}")

    def sleep(self):
        print(f"{self.name} sleeps.")
        self.energie += 25
        print(f"{self.name} sleeping and his energy is: {self.energy}")


    def eats(self):
        print(f"{self.name} eats.")
        self.energy += 5
        self.health +- 10
        print(f"{self.name} eating and his energy is: {self.energy} and his health is: {self.health}")

    def play(self):
        print(f"{self.name} plays.")
        self.health += 5
        print(f"{self.name} increases health by: {self.health}")

    def noise(self):
        print(f"{self.name} make a noise.")

ninja_1 = Ninja("Baraa","Hedri", "Biscuits", "Croquettes", Pet("Fluffy", "Dog", "Fetch"))


ninja_1.walks()
ninja_1.feeds()
ninja_1.bathe()