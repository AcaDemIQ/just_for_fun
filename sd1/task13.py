#!/usr/bin/env python3.14t

def abs(x):
    if x < 0:
        return -x
    return x
# Prooves
# {P: x < 0} x = abs(x) {Q : x > 0}
# {P: x >= 0} x = abs(x) {Q : x > 0}


def max(a, b):
    if a > b:
        return a
    return b
#Prooves
# {P: a > b} r = max(a,b) {Q: r == a}
# {P: a <= b} r = max(a,b) {Q: r == b}

def compose(a,b):
    return max(abs(a), abs(b))


if __name__ == "__main__":
    print(compose(-5,2))
    # Prooves
    # {P : a > 0 && b > 0 && a > b } r = compose(a,b) {Q : r==a}
    # {P : a > 0 && b > 0 && a <= b } r = compose(a,b) {Q : r==b}
    # {P : a > 0 && b <= 0 && a > -b } r = compose(a,b) {Q : r==a}
    # {P : a > 0 && b <= 0 && a <= -b } r = compose(a,b) {Q : r==-b}
    # {P : a <= 0 && b <= 0 && -a > -b } r = compose(a,b) {Q : r==-a}
    # {P : a <= 0 && b <= 0 && -a <= -b } r = compose(a,b) {Q : r==-b}
    # {P : a <= 0 && b > 0 && -a > b } r = compose(a,b) {Q : r==-a}
    # {P : a <= 0 && b > 0 && -a <= b } r = compose(a,b) {Q : r==b}
