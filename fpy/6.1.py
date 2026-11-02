from pymonad.tools import curry
from pymonad.state import State
from math import sin, pi


# Вычислять sin на каждом шаге и считать количество запусков

@curry(2)
def state_sin(arg, last):
    def compute(sin_count):
        print(last)
        return sin(arg), sin_count + 1
    return State(compute)

user_state = State.insert(0)


final = user_state.then(state_sin(0)).then(state_sin(pi / 2)).then(state_sin(2*pi))

print(final.run(0))
