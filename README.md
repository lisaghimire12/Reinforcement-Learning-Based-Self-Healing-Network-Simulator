Mininet → Python RL Agent → Linux Firewall (iptables)
                          → Traffic Control (tc)

h1 → normal user
h2 → normal user
server → target
attacker → attacker machine
s1 → switch

1. Created a software-defined test network, nothing touches the real internet. It’s a safe sandbox.
This is the foundation for:
➡ Simulating attacks
➡ Monitoring traffic
➡ Training RL agent
➡ Automatically blocking attacker

Before AI can learn anything, it needs traffic.
So next we make:
➡ Normal traffic
➡ Attack traffic

Generate Normal Traffic
Inside Mininet, we simulate legitimate users accessing server.
Example actions:
h1 ping server
h2 ping server
h1 wget http://server

Generate Attack Traffic
From attacker node:
Flood pings
Repeated connection attempts
Packet bursts
Example:
attacker ping server -f

Capture Traffic
We start monitoring packets:
Packet rate
Source IP
Destination IP
Protocol

Build Reinforcement Learning Environment
State → traffic features
Actions → block IP, allow, throttle
Reward → attack reduced or not

Automatic Blocking
When agent decides:
➡ Block attacker
We execute:
iptables -A INPUT -s attacker_ip -j DROP


# To enable mininet:
sudo python3 topology.py
mininet> h1 ping server
mininet> attacker ping server

# Traffic monitor module
The system must see traffic before it can think.
File name:
monitor.py
Run:sudo python3 monitor.py

# RUN:
TERMINAL 1 — Start Network
source venv/bin/activate
cd ~/Desktop/NIS
sudo python3 topology.py

TERMINAL 2 — Start Monitor
cd ~/Desktop/NIS
sudo ./venv/bin/python monitor.py

attacker ping server -i 0.01


If packet_count[ip] > 200
→ Consider attacker
→ Block IP using firewall
Traffic → Monitor → Threshold Check → Block IP

# RL AGENT
Attack exists & agent blocks +10
Attack exists & agent does nothing -10
No attack & agent does nothing +5
No attack & agent blocks -5


Traffic → Monitor → Detect Attack → Block Attacker Automatically


# CHANGE OF MIND-ARCHITECTURE:
React Dashboard
     |
FastAPI Backend
     |
Network Environment
     |
Attack Simulator
     |
RL Agent
     |
Firewall Controller

# THRESHOLD-30

Installl Fast API:
pip install fastapi uvicorn

RUN:
uvicorn backend.app:app --reload
npm run dev