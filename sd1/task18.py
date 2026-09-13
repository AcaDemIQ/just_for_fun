#!/usr/bin/env python3.14t


class IntParam:
    def check(self, value):
        if type(value) == int:
            return True
        return False

    def generate_obj(self, value):
        return {"type": "int", "value": value}


class FloatParam:
    def check(self, value):
        if type(value) == float:
            return True
        return False

    def generate_obj(self, value):
        return {"type": "float", "value": value}


class ParamsManager:
    def __init__(self):
        self.arr = [IntParam(), FloatParam()]

    def generate_obj(self, value):
        res = list(filter(lambda l: l["status"], map(lambda i: {"num": i[0], "status": i[1].check(value)}, enumerate(self.arr))))
        if len(res) == 1:
            return self.arr[res[0]["num"]].generate_obj(value)
        else:
            return None



if __name__ == "__main__":
    manager = ParamsManager()
    print(manager.generate_obj(4))
