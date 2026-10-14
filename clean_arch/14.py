import math
from collections import namedtuple

RobotState = namedtuple("RobotState", "x y angle state")

# режимы работы устройства очистки
WATER = 1 # полив водой
SOAP  = 2 # полив мыльной пеной
BRUSH = 3 # чистка щётками


# взаимодействие с роботом вынесено в отдельную функцию
def transfer_to_cleaner(message):
    print (message)

# перемещение
def move(dist):
    def func(state):
        angle_rads = state.angle * (math.pi/180.0)   
        new_state = RobotState(
            state.x + dist * math.cos(angle_rads),
            state.y + dist * math.sin(angle_rads),
            state.angle,
            state.state)  
        return ([f'POS({new_state.x},{new_state.y})'], new_state)
    return func

# поворот
def turn(turn_angle):
    def func(state):
        new_state = RobotState(
            state.x,
            state.y,
            state.angle + turn_angle,
            state.state)
        return ([f'ANGLE {new_state.angle}'], new_state)
    return func

# установка режима работы
def set_state(new_internal_state):
    def func(state):
        if new_internal_state=='water':
            self_state = WATER  
        elif new_internal_state=='soap':
            self_state = SOAP
        elif new_internal_state=='brush':
            self_state = BRUSH
        else:
            return (["no mod"], state)  
        new_state = RobotState(
            state.x,
            state.y,
            state.angle,
            self_state)
        return ([f'STATE {self_state}'], new_state)
    return func

# начало чистки
def start():
    def func(state):
        return ([f'START WITH {state.state}'], state)
    
    return func

# конец чистки
def stop():
    return lambda state: (['STOP'], state)


class LazyMonadState():
    def __init__(self, state=RobotState(0.0, 0.0, 0, None), log=[], methods=[]):
        self.state = state
        self.log = log
        self.methods = methods

    @classmethod
    def pure(cls, state):
        return LazyMonadState(state)

    def bind(self, func):
        return LazyMonadState(self.state, self.log, [*self.methods, func])

    def _calc(self):
        for func in self.methods:
            new_value = func(self.state)
            self.state = new_value[1]
            self.log = [*self.log, *new_value[0]]
        self.methods = []


    def get_log(self):
        if len(self.methods) > 0:
            self._calc()
        return self.log

    def get_state(self):
        if len(self.methods) > 0:
            self._calc()
        return self.state

# интерпретация набора команд
def make(code,state = RobotState(0.0, 0.0, 0, None)):
    state = LazyMonadState.pure(state)
    for command in code:
        cmd = command.split(' ')
        if cmd[0]=='move':
            state = state.bind(move(int(cmd[1])))
        elif cmd[0]=='turn':
            state = state.bind(turn(int(cmd[1])))
        elif cmd[0]=='set':
            state = state.bind(set_state(cmd[1])) 
        elif cmd[0]=='start':
            state = state.bind(start())
        elif cmd[0]=='stop':
            state = state.bind(stop())
    return state



if __name__ == "__main__":
    # Клиентская часть
    code = ['move 5', 'turn -90', 'move 5', 'set soap', 'start', 'move 10', 'stop']
    new_state = make(code)
    print(new_state.get_log())
    print(new_state.get_state())


