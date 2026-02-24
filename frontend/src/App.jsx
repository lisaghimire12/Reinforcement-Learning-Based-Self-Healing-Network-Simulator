import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState({
    state: 0,
    action: 0,
    reward: 0
  });

  useEffect(() => {
    const interval = setInterval(async () => {
      const res = await fetch("http://127.0.0.1:8000/status");
      const json = await res.json();

      setData({
        state: json.state,
        action: json.action,
        reward: json.reward
      });
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const toggleAttack = async () => {
    await fetch("http://127.0.0.1:8000/toggle_attack", {
      method: "POST"
    });
  };

  return (
    <div className="container">
      <h1 className="title">⚡ Self-Healing Network AI</h1>

      <div className="grid">
        <div className="card blue">
          <h2>Traffic</h2>
          <p>{data.state}</p>
        </div>

        <div className={`card ${data.action === 1 ? "red" : "green"}`}>
          <h2>Agent Action</h2>
          <p>{data.action === 1 ? "BLOCK" : "ALLOW"}</p>
        </div>

        <div className="card purple">
          <h2>Reward</h2>
          <p>{data.reward}</p>
        </div>
      </div>

      <div className="btn-wrapper">
        <button className="attack-btn" onClick={toggleAttack}>
          🚨 Toggle Attack
        </button>
      </div>
    </div>
  );
}

export default App;