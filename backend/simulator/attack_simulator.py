import random

class AttackSimulator:
    def __init__(self):
        self.attack_on = False

    def toggle_attack(self):
        self.attack_on = not self.attack_on

    def generate_traffic(self):
        if self.attack_on:
            return random.randint(60,120)   # attack traffic
        return random.randint(5,25)         # normal traffic