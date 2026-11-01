from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

add10 = add(10)

print(Maybe.apply(add10).to_arguments(Just(3)))

print(ListMonad(1,2,3,4).map(add10))

print(Nothing.then(add10))
