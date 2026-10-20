from dataclasses import dataclass
from typing import List, Protocol, Any
from enum import Enum
import math
from functools import partial


# Состояние робота
@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    state: int

# Режимы работы
class CleaningMode(Enum):
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
    
    if round(x) == constrained_x and round(y) == constrained_y:
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



# Конкретные команды
@dataclass
class Move:
    distance: float
    
    def interpret(self, state: RobotState) -> (RobotState, bool):
        angle_rads = state.angle * (math.pi/180.0)
        return (RobotState(
            x=state.x + self.distance * math.cos(angle_rads),
            y=state.y + self.distance * math.sin(angle_rads),
            angle=state.angle,
            state=state.state
        ), True) if check_position(state.x + self.distance * math.cos(angle_rads), state.y + self.distance * math.sin(angle_rads))[2] != MoveResponse.BARRIER else (state, False)

    def next(self, response, succ=None):
        if not response:
            return Stop()
        else:
            return succ

    
@dataclass
class Turn:
    angle: float
    
    def interpret(self, state: RobotState) -> (RobotState, bool):
        return (RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle + self.angle,
            state=state.state
        ), True)

    def next(self, response, succ=None):
        return succ
    
@dataclass
class SetState:
    new_state: CleaningMode
    
    def interpret(self, state: RobotState) -> (RobotState, bool):
        return (RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle,
            state=self.new_state.value
        ), True)

    def next(self, response, succ=None):
        return succ


@dataclass
class Stop:
    def interpret(self, state):
        pass

    def next(self, response):
        pass




if __name__ == "__main__":
    # Создание и объединение комманд в цепочку
    move1 = Move(50)

    turn1 = Turn(-180)
    set1 = SetState(CleaningMode.SOAP)
    move2= Move(40)
    stop = Stop()
    # Немного коряво -- надо было бы в отдельной функции сделать
    move1.next = partial(move1.next, succ=turn1)
    turn1.next = partial(turn1.next, succ=set1)
    set1.next = partial(set1.next, succ=move2)
    move2.next = partial(move2.next, succ=stop)

    # Сам интерпретатор
    current_step = move1
    state = RobotState(0.0, 0.0, 0, None)
    print(state)
    print(type(current_step))
    while type(current_step) is not Stop:
        state, status = current_step.interpret(state)
        print(state)
        print(status)
        current_step = current_step.next(status)
        print(type(current_step))
        



