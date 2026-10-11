import pure_robot

class RobotTask():
    def __init__(self, transfer = pure_robot.transfer_to_cleaner):
        self.transfer = transfer
        self.state = pure_robot.RobotState(0,0,0,None)
        self.tasks = []

    def add_move(self, dist):
        self.tasks.append(f'move {dist}')
        return self

    def add_turn(self, angle):
        self.tasks.append(f'turn {angle}')
        return self

    def add_set_state(self, state):
        self.tasks.append(f'set {state}')
        return self

    def add_start(self):
        self.tasks.append('start')
        return self

    def add_stop(self):
        self.tasks.append('stop')
        return self

    def execute(self):
        self.state = pure_robot.make(self.transfer, self.tasks, self.state)
        return self


if __name__ == "__main__":
    robot = RobotTask()
    robot.add_move(5)\
        .add_turn(-90)\
        .add_move(5)\
        .add_set_state('soap')\
        .add_start()\
        .add_move(10)\
        .add_stop()\
        .execute()
    print(robot.state)
