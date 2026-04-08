import requests
import random

BASE_URL = "http://127.0.0.1:8000"

print("[START]")

requests.post(BASE_URL + "/reset")

for i in range(10):

    action = random.randint(0,3)

    response = requests.post(
        BASE_URL + "/step",
        json={"move":action}
    )

    print("[STEP]", response.json())

print("[END]")