#Koy Saechao
#Robot vs Dinosaur


from weapon import Weapons

class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapons["machine gun", "laser gun", "freezer gun"]

    def attack_you(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_you
        print("SUCCESSFUL ATTACK!!! Dinosaur health level is now {dinosaur.health}")

