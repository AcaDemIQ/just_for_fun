#!/usr/bin/env python3.14t

import random
import threading
import functools
import concurrent.futures


SIZE=1000000
THREADS=4
CHUNK_SIZE= SIZE // THREADS
MIN_VALUE = 1
MAX_VALUE = 100
DATA = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]


def func(start, end):
    return functools.reduce(lambda s, i: s + DATA[i], range(start, end))    

if __name__ == "__main__":
    sum_value = 0
    with concurrent.futures.ThreadPoolExecutor(THREADS) as executor:
        futures = [executor.submit(func, i * CHUNK_SIZE, (i+1) * CHUNK_SIZE) for i in range(THREADS)]
        results = [f.result() for f in futures]
        sum_value = functools.reduce(lambda s, i: s + i, results)
    print(sum_value)






