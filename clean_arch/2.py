import math
from enum import Enum


position=(0,0)
vec=(1,0) # единичный вектор направления, его будем менять

Work = Enum('Work', [('no', 1), ('water', 2), ('soap', 3), ('brush', 4)])
current_work = Work.no
working_flag = False


def move(step: int) -> None:
    global position
    global vec
    position = (position[0] + vec[0] * step, position[1] + vec[1] * step)
    print(f"POS {position[0]} {position[1]}")

def turn(grad: int) -> None:
    global vec
    rad = grad * math.pi /  180
    vec = (vec[0]*math.cos(rad) - vec[1]*math.sin(rad), vec[0]*math.sin(rad) + vec[1]*math.cos(rad))
    new_grad = math.acos(vec[0]) * 180 / math.pi
    print(f"ANGLE {new_grad}")


def set(_work: str) -> None:
    global current_work
    current_work = Work[_work]
    print(f'STATE {current_work.name}')

def start():
    global current_work
    global working_flag
    working_flag = True
    print(f'START WITH {current_work.name}')

def stop():
    global current_work
    global working_flag
    working_flag = False
    current_work = Work.no
    print(f'STOP')



commands = [
        'move 5',
        'turn 90',
        'move 5',
        'set soap',
        'start',
        'move 50',
        'stop'
]


def main_loop(commands):
    for c in commands:
        if c.startswith('move'):
            move(int(c.split(' ')[1]))
        elif c.startswith('turn'):
            turn(int(c.split(' ')[1]))
        elif c.startswith('set'):
            set(c.split(' ')[1])
        elif c == "start":
            start()
        elif c == "stop":
            stop()
        else:
            raise ValueError("No command found")


if __name__ == "__main__":
    main_loop(commands)
