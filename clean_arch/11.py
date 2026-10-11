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
def move(transfer,dist,state):
    angle_rads = state.angle * (math.pi/180.0)   
    new_state = RobotState(
        state.x + dist * math.cos(angle_rads),
        state.y + dist * math.sin(angle_rads),
        state.angle,
        state.state)  
    transfer(('POS(',new_state.x,',',new_state.y,')'))
    return new_state

# поворот
def turn(transfer,turn_angle,state):
    new_state = RobotState(
        state.x,
        state.y,
        state.angle + turn_angle,
        state.state)
    transfer(('ANGLE',state.angle))
    return new_state

# установка режима работы
def set_state(transfer,new_internal_state,state):
    if new_internal_state=='water':
        self_state = WATER  
    elif new_internal_state=='soap':
        self_state = SOAP
    elif new_internal_state=='brush':
        self_state = BRUSH
    else:
        return state  
    new_state = RobotState(
        state.x,
        state.y,
        state.angle,
        self_state)
    transfer(('STATE',self_state))
    return new_state

# начало чистки
def start(transfer,state):
    transfer(('START WITH',state.state))
    return state

# конец чистки
def stop(transfer,state):
    transfer(('STOP',))
    return state

def base_operation_exec(action, *args):
    match action:
        case "move":
            return move(*args)
        case "turn":
            return turn(*args)
        case 'set':
            return set_state(*args)
        case 'start':
            return start(*args)
        case 'stop':
            return stop(*args)

# интерпретация набора команд
def make(exec_func, transfer,code,state):
    for command in code:
        cmd = command.split(' ')
        if cmd[0]=='move':
            state = exec_func('move', transfer,int(cmd[1]),state) 
        elif cmd[0]=='turn':
            state = exec_func('turn', transfer,int(cmd[1]),state)
        elif cmd[0]=='set':
            state = exec_func('set', transfer,cmd[1],state) 
        elif cmd[0]=='start':
            state = exec_func('start', transfer,state)
        elif cmd[0]=='stop':
            state = exec_func('stop', transfer,state)
    return state



if __name__ == "__main__":
    code = ['move 5', 'turn -90', 'move 5', 'set soap', 'start', 'move 10', 'stop']
    new_state = make(base_operation_exec, transfer_to_cleaner, code, RobotState(0.0, 0.0, 0, None))

