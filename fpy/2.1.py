from pymonad.tools import curry

@curry(2)
def print_two_str(a, b):
    return a + b


print_hello = print_two_str("Hello, ")
print(print_hello("Alex"))
