#!/usr/bin/env python3.14t


import concurrent
import time
from concurrent.futures import ThreadPoolExecutor

def work(a, b):
    return a * b

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as pool:
        arr = []
        for i in range(8):
            arr.append(pool.submit(work, i, i*2))
        res = 0
        for a in arr:
            res = a.result() + res
        print(res)




