from backend.simulator.attack_simulator import AttackSimulator
from backend.firewall.controller import FirewallController

class NetworkEnv:
    def __init__(self):
        self.attack_sim = AttackSimulator()
        self.firewall = FirewallController()
        self.threshold = 30

    def get_state(self):
        traffic = self.attack_sim.generate_traffic()
        return traffic

    def step(self, action):
        state = self.get_state()

        attack = state > self.threshold

        if action == 1:
            self.firewall.block()

        if attack and action == 1:
            reward = 10
        elif attack and action == 0:
            reward = -10
        elif not attack and action == 0:
            reward = 5
        else:
            reward = -5

        return state, reward