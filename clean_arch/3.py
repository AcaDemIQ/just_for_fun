import math
from enum import Enum



Work = Enum('Work', [('no', 1), ('water', 2), ('soap', 3), ('brush', 4)])


def transfer_to_outside(message):
    print(message)

class Robot:
    def __init__(self):
        self.position=(0,0)
        self.vec=(1,0) # единичный вектор направления, его будем менять
        self.current_work = Work.no
        self.working_flag = False

    def move(self, step: int) -> None:
        self.position = (self.position[0] + self.vec[0] * step, self.position[1] + self.vec[1] * step)
        transfer_to_outside(f"POS {self.position[0]} {self.position[1]}")

    def turn(self, grad: int) -> None:
        rad = grad * math.pi /  180
        self.vec = (self.vec[0]*math.cos(rad) - self.vec[1]*math.sin(rad), self.vec[0]*math.sin(rad) + self.vec[1]*math.cos(rad))
        new_grad = math.acos(self.vec[0]) * 180 / math.pi
        transfer_to_outside(f"ANGLE {new_grad}")


    def set(self, _work: str) -> None:
        self.current_work = Work[_work]
        transfer_to_outside(f'STATE {self.current_work.name}')

    def start(self):
        self.working_flag = True
        transfer_to_outside(f'START WITH {self.current_work.name}')

    def stop(self):
        self.working_flag = False
        self.current_work = Work.no
        transfer_to_outside(f'STOP')



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
    robot = Robot()
    for c in commands:
        if c.startswith('move'):
            robot.move(int(c.split(' ')[1]))
        elif c.startswith('turn'):
            robot.turn(int(c.split(' ')[1]))
        elif c.startswith('set'):
            robot.set(c.split(' ')[1])
        elif c == "start":
            robot.start()
        elif c == "stop":
            robot.stop()
        else:
            raise ValueError("No command found")


if __name__ == "__main__":
    main_loop(commands)
