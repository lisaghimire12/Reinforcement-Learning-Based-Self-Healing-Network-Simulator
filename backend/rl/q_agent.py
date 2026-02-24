import random

class QLearningAgent:
    def __init__(self):
        self.q = {}
        self.alpha = 0.2
        self.gamma = 0.9
        self.epsilon = 0.5

    def get_q(self, s, a):
        return self.q.get((s,a), 0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([0,1])
        return 1 if self.get_q(state,1) > self.get_q(state,0) else 0

    def update(self, s, a, r, ns):
        old = self.get_q(s,a)
        best_next = max(self.get_q(ns,0), self.get_q(ns,1))
        self.q[(s,a)] = old + self.alpha*(r + self.gamma*best_next - old)