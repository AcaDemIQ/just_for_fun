import math
from enum import Enum

Work = Enum('Work', [('no', 1), ('water', 2), ('soap', 3), ('brush', 4)])


class Robot:
    def __init__(self, f):
        self.position=(0,0)
        self.vec=(1,0) # единичный вектор направления, его будем менять
        self.current_work = Work.no
        self.working_flag = False
        self.transfer = f

    def move(self, step: int) -> None:
        self.position = (self.position[0] + self.vec[0] * step, self.position[1] + self.vec[1] * step)
        self.transfer(f"POS {self.position[0]} {self.position[1]}")

    def turn(self, grad: int) -> None:
        rad = grad * math.pi /  180
        self.vec = (self.vec[0]*math.cos(rad) - self.vec[1]*math.sin(rad), self.vec[0]*math.sin(rad) + self.vec[1]*math.cos(rad))
        new_grad = math.acos(self.vec[0]) * 180 / math.pi
        self.transfer(f"ANGLE {new_grad}")


    def set(self, _work: str) -> None:
        self.current_work = Work[_work]
        self.transfer(f'STATE {self.current_work.name}')

    def start(self):
        self.working_flag = True
        self.transfer(f'START WITH {self.current_work.name}')

    def stop(self):
        self.working_flag = False
        self.current_work = Work.no
        self.transfer(f'STOP')



