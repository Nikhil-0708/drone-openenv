import numpy as np

class DroneEnvironment:

    def __init__(self):
        self.grid_size = 5
        self.goal = [4,4]
        self.position = [0,0]

    def reset(self):

        self.position = [0,0]

        return {
            "x": self.position[0],
            "y": self.position[1],
            "reward": 0
        }

    def step(self, move):

        if move == 0:
            self.position[0] += 1

        elif move == 1:
            self.position[0] -= 1

        elif move == 2:
            self.position[1] += 1

        elif move == 3:
            self.position[1] -= 1

        self.position = list(np.clip(
            self.position,
            0,
            self.grid_size-1
        ))

        reward = 0

        if self.position == self.goal:
            reward = 1

        return {
            "x": int(self.position[0]),
            "y": int(self.position[1]),
            "reward": reward
        }