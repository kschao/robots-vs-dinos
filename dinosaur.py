#Koy Saechao
#Robot vs Dinosaur


class Dinosaurs:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_you = 20

    def attack(self, robot):
        robot.health = robot.health - self.attack_you
        print("SUCCESSFUL ATTACK!!! Robot health level is now {robot.health}")
            
