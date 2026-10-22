import math
from enum import Enum



Work = Enum('Work', [('no', 1), ('water', 2), ('soap', 3), ('brush', 4)])


def transfer_to_outside(message):
    print(message)

class Robot:
    def __init__(self, f, pos=(0,0), vec=(1,0), current_work=Work.no, working_flag=False):
        self.position = pos
        self.vec=vec # единичный вектор направления, его будем менять
        self.current_work = current_work
        self.working_flag = working_flag
        self.transfer = f

    def move(self, step: int) -> Robot:
        position = (self.position[0] + self.vec[0] * step, self.position[1] + self.vec[1] * step)
        self.transfer(f"POS {position[0]} {position[1]}")
        return Robot(self.transfer, pos=position, vec=self.vec, current_work=self.current_work, working_flag=self.working_flag)

    def turn(self, grad: int) -> Robot:
        rad = grad * math.pi /  180

        new_vec = (self.vec[0]*math.cos(rad) - self.vec[1]*math.sin(rad), self.vec[0]*math.sin(rad) + self.vec[1]*math.cos(rad))
        new_grad = math.acos(new_vec[0]) * 180 / math.pi
        self.transfer(f"ANGLE {new_grad}")
        return Robot(self.transfer, pos=self.position, vec=new_vec, current_work=self.current_work, working_flag=self.working_flag)

    def set(self, _work: str) -> None:
        new_current_work = Work[_work]
        self.transfer(f'STATE {new_current_work.name}')
        return Robot(self.transfer, pos=self.position, vec=self.vec, current_work=new_current_work, working_flag=self.working_flag)

    def start(self):
        
        self.transfer(f'START WITH {self.current_work.name}')
        return Robot(self.transfer, pos=self.position, vec=self.vec, current_work=self.current_work, working_flag=True)

    def stop(self):
        self.transfer(f'STOP')
        return Robot(self.transfer, pos=self.position, vec=self.vec, current_work=Work.no, working_flag=False)



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
    robot = Robot(transfer_to_outside)
    for c in commands:
        if c.startswith('move'):
            robot = robot.move(int(c.split(' ')[1]))
        elif c.startswith('turn'):
            robot = robot.turn(int(c.split(' ')[1]))
        elif c.startswith('set'):
            robot = robot.set(c.split(' ')[1])
        elif c == "start":
            robot = robot.start()
        elif c == "stop":
            robot = robot.stop()
        else:
            raise ValueError("No command found")


if __name__ == "__main__":
    main_loop(commands)
