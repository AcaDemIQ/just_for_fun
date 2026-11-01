from pymonad.tools import curry


def print_four(start, start_sym, end, end_sym):
    return f'{start}{start_sym} {end}{end_sym}'

@curry(4)
def first_step(start, start_sym, end_sym, end):
    return print_four(start, start_sym, end, end_sym)



final = first_step("Hello")(",")("!")
print(final("Petya"))

