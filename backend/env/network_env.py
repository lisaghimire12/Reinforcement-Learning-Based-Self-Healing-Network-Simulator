from backend.simulator.attack_simulator import AttackSimulator
from backend.firewall.controller import FirewallController

class NetworkEnv:
    def __init__(self):
        self.attack_sim = AttackSimulator()
        self.firewall = FirewallController()
        self.threshold = 30
        self.current_state = 0

    def reset(self):
        self.current_state = self.attack_sim.generate_traffic()
        return self.current_state

    def step(self, action):
        attack = self.current_state > self.threshold

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

        next_state = self.attack_sim.generate_traffic()
        self.current_state = next_state

        return next_state, reward