import pure_robot
from abc import ABCMeta, abstractmethod, abstractproperty

class CleanerApi():
    __metaclass__=ABCMeta

    @abstractproperty
    def get_state(self):
        pass

    @abstractproperty
    def get_angle(self):
        pass

    @abstractproperty
    def get_x(self):
        pass

    @abstractproperty
    def get_y(self):
        pass

    @abstractmethod
    def transfer_to_cleaner(self,message):
        pass

    @abstractmethod
    def activate_cleaner(self, code):
        pass

# класс Чистильщик API
class CleanerApiImpl(CleanerApi):

    # конструктор 
    def __init__(self):
        self.cleaner_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)

    # взаимодействие с роботом вынесено в отдельную функцию
    def transfer_to_cleaner(self,message):
        print (message)

    def get_x(self):
        return self.cleaner_state.x

    def get_y(self):
        return self.cleaner_state.y

    def get_angle(self):
        return self.cleaner_state.angle

    def get_state(self):
        return self.cleaner_state.state

    def activate_cleaner(self,code):
        for command in code:
            cmd = command.split(' ')
            if cmd[0]=='move':
                self.cleaner_state = pure_robot.move(self.transfer_to_cleaner,
                    int(cmd[1]),self.cleaner_state) 
            elif cmd[0]=='turn':
                self.cleaner_state = pure_robot.turn(self.transfer_to_cleaner,
                    int(cmd[1]),self.cleaner_state)
            elif cmd[0]=='set':
                self.cleaner_state = pure_robot.set_state(self.transfer_to_cleaner,
                    cmd[1],self.cleaner_state) 
            elif cmd[0]=='start':
                self.cleaner_state = pure_robot.start(self.transfer_to_cleaner,
                    self.cleaner_state)
            elif cmd[0]=='stop':
                self.cleaner_state = pure_robot.stop(self.transfer_to_cleaner,
                    self.cleaner_state)



if __name__ == "__main__":
    print(issubclass(CleanerApiImpl, CleanerApi))
    print(isinstance(CleanerApiImpl(), CleanerApi))
