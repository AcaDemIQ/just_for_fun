from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

to_left = lambda num: lambda p: (
    Nothing
    if abs((p[0] + num) - p[1]) > 4
    else Just((p[0] + num, p[1]))
)

# посадка птиц на правую сторону
to_right = lambda num: lambda p: (
    Nothing
    if abs((p[1] + num) - p[0]) > 4
    else Just((p[0], p[1] + num))
)

# банановая кожура
banana = lambda x: Nothing


begin = lambda: Just( (0,0) )

def show(a):
    if a.is_just():
        print(a.value)
    else:
        print("Nonono")


show(begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-2)))

show(begin().bind(to_left(2)).bind(to_right(5)).bind(to_left(-1)))


show(begin().bind(to_left(2)).bind(banana).bind(to_right(5)).bind(to_left(-1)))



