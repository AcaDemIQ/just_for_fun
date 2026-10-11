import pure_robot

class RobotTask():

    def init_state(self):
        return pure_robot.RobotState(0.0, 0.0, 0, None)

    def add_move(self, tasks, dist):
        return [*tasks, f'move {dist}']
        

    def add_turn(self, tasks, angle):
        return [*tasks, f'turn {angle}']
        

    def add_set_state(self, tasks, state):
        return [*tasks, f'set {state}']
    

    def add_start(self, tasks):
        return [*tasks, 'start']

    def add_stop(self, tasks):
        return [*tasks, 'stop']

    def execute(self, tasks, state):
        return pure_robot.make(pure_robot.transfer_to_cleaner, tasks, state)


if __name__ == "__main__":
    robot = RobotTask()
    print(robot.execute(robot.add_stop(
            robot.add_move(robot.add_start(robot.add_set_state(robot.add_move(robot.add_turn(robot.add_move([], 5), -90), 5), 'wash'))
                , 5)
        ), robot.init_state()))
