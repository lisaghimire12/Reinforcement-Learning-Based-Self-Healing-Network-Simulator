from fastapi import FastAPI
from backend.env.network_env import NetworkEnv
from backend.rl.q_agent import QLearningAgent
import threading
import time

app = FastAPI()

env = NetworkEnv()
agent = QLearningAgent()

latest_data = {
    "state": 0,
    "action": 0,
    "reward": 0
}

# -------------------------------
# Background RL Training Loop
# -------------------------------

def training_loop():
    while True:
        state = env.get_state()
        action = agent.choose_action(state)
        next_state, reward = env.step(action)
        agent.update(state, action, reward, next_state)

        latest_data["state"] = state
        latest_data["action"] = action
        latest_data["reward"] = reward

        time.sleep(1)

# -------------------------------
# Start loop when server starts
# -------------------------------

@app.on_event("startup")
def start_training():
    t = threading.Thread(target=training_loop)
    t.daemon = True
    t.start()

# -------------------------------
# API ENDPOINTS
# -------------------------------

@app.get("/status")
def get_status():
    return latest_data

@app.post("/toggle_attack")
def toggle_attack():
    env.attack_sim.toggle_attack()
    return {"message": "Attack state toggled"}