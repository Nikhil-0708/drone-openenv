from fastapi import FastAPI
from server.drone_env import DroneEnvironment

app = FastAPI()

env = DroneEnvironment()

@app.post("/reset")
def reset():

    return env.reset()


@app.post("/step")
def step(action: dict):

    move = action["move"]

    return env.step(move)

@app.get("/state")
def state():
    return {"status": "running"}
