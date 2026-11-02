from pymonad.tools import curry
from pymonad.state import State
from math import sin, pi
from copy import deepcopy
from itertools import chain



@curry(3)
def state_next(n, m, last):
    def compute(count):
        # Тут и происходит монадическая магия: сначала через map получаем список всевозможных занятых позиций на след шаге (без проверки)
        # Затем, тк у нас получается уже список списков (!!!), нам нужно сделать flatten, использую chain.from_iterable
        # Потом уже -- проверка на границы
        # Под самый конец -- выявление уникальных значений и формулировка нового списка из уникальных позиций
        current = list(set(filter(lambda a: a[0] <= n and a[0] >= 1 and a[1] <= m and a[1] >= 1, chain.from_iterable(map(lambda a: [(a[0], a[1]), (a[0] + 1, a[1]), (a[0]-1, a[1]), (a[0], a[1]+1), (a[0], a[1]-1)], last)))))
        return current, count + 1
    return State(compute)

def init_func(n, m, func):
    max_value = n*m
    return func(n, m), max_value

state_next, max_value = init_func(3, 4, state_next)

def loop(value, state, func, max_value):
    # формально я бы мог использовать for для генератора, но по тексту задания -- "циклы" нельзя
    final = value.then(func)
    res = final.run(state)
    if len(res[0]) != max_value: # пока не заняли все возможные клетки
        return loop(State.insert(res[0]), res[1], func, max_value)
    else:
        return res[1]


print(loop(State.insert([(2,2), (3,4)]), 1, state_next, max_value))
