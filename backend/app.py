from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.env.network_env import NetworkEnv
from backend.rl.q_agent import QLearningAgent
import threading
import time

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    state = env.reset()

    while True:
        action = agent.choose_action(state)
        next_state, reward = env.step(action)
        agent.update(state, action, reward, next_state)

        latest_data["state"] = state
        latest_data["action"] = action
        latest_data["reward"] = reward

        state = next_state
        time.sleep(1)
        print("DEBUG:", latest_data)
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