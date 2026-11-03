from functools import reduce


seq = [5,4,3,2,5]
def init(seq):
    if seq[0] < seq[1]:
        return (seq[1], seq[0])
    else:
        return (seq[0], seq[1])


init_seq = init(seq)

def step(t, a):
    t = list(t)
    if a > t[0]:
        t[1] = t[0]
        t[0] = a
    elif a > t[1] and a <= t[0]:
        t[1] = a
    return tuple(t)


print(reduce(step, seq[2:], initial=init_seq)[1])
