from robot import Robot

def transfer_to_outside(message):
    print(message)


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
