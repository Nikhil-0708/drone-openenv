from dataclasses import dataclass

@dataclass
class DroneAction:
    move: int

@dataclass
class DroneObservation:
    x: int
    y: int
    reward: float

@dataclass
class DroneState:
    step_count: int = 0