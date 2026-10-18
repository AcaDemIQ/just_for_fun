from functools import wraps
from collections import namedtuple
import math

RobotState = namedtuple("RobotState", "x y angle state")


WATER = 1  
SOAP = 2   
BRUSH = 3  

class MoveResponse:
    OK = "MOVE_OK"
    BARRIER = "HIT_BARRIER"

class SetStateResponse:
    OK = "STATE_OK"
    NO_WATER = "OUT_OF_WATER"
    NO_SOAP = "OUT_OF_SOAP"


def check_position(x: float, y: float) -> tuple[float, float, str]:
    constrained_x = max(0, min(100, x))
    constrained_y = max(0, min(100, y))
    
    if x == constrained_x and y == constrained_y:
        return (x, y, MoveResponse.OK)
    return (constrained_x, constrained_y, MoveResponse.BARRIER)

water_level = 100
has_soap = True
def check_resources(new_mode: int) -> SetStateResponse:
    global water_level
    global has_soap
    if new_mode == WATER:
        if water_level == 0:
            return SetStateResponse.NO_WATER
        water_level -= 50
    elif new_mode == SOAP:
        if not has_soap:
            return SetStateResponse.NO_SOAP
        has_soap = False
    return SetStateResponse.OK

class StateMonad:
    def __init__(self, state, log=None):
        self.state = state
        self.log = log or []
    
    def bind(self, func):
        new_state, new_log = func(self.state, self.log)
        return StateMonad(new_state, new_log)

def move(dist):
    def inner(old_state, log):
        angle_rads = old_state.angle * (math.pi/180.0)
        
        
        check_state = check_position(old_state.x + dist * math.cos(angle_rads), old_state.y + dist * math.sin(angle_rads))
    
        if check_state[2] != MoveResponse.OK:
            return RobotState(check_state[0], check_state[1], old_state.angle, old_state.state), log + [f'POS BARRIER({int(check_state[0])},{int(check_state[1])})']
        new_state = RobotState(
            old_state.x + dist * math.cos(angle_rads),
            old_state.y + dist * math.sin(angle_rads),
            old_state.angle,
            old_state.state
        )
        return new_state, log + [f'POS({int(new_state.x)},{int(new_state.y)})']
    return inner

def turn(angle):
    def inner(old_state, log):
        new_state = RobotState(
            old_state.x,
            old_state.y,
            old_state.angle + angle,
            old_state.state
        )
        return new_state, log + [f'ANGLE {new_state.angle}']
    return inner

def set_state(new_mode):
    def inner(old_state, log):
        if check_resources(new_mode) != SetStateResponse.OK:
            return old_state, log + [f'NOT SET TO {new_mode}']
        new_state = RobotState(
            old_state.x,
            old_state.y,
            old_state.angle,
            new_mode
        )
        return new_state, log + [f'STATE {new_mode}']
    return inner

def start(old_state, log):
    return old_state, log + ['START']

def stop(old_state, log):
    return old_state, log + ['STOP']


initial_state = StateMonad(RobotState(0.0, 0.0, 0, WATER))
result = (initial_state
    .bind(move(100))
    .bind(turn(-90))
    .bind(set_state(SOAP))
    .bind(start)
    .bind(move(50))
    .bind(stop))

print(f"Final state: {result.state}")
print(f"Log: {result.log}")



