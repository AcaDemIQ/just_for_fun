#!/usr/bin/env python3.14t


import time
import threading

# MapReduce solution

barrier = threading.Barrier(6)
array = [-1,-1,-1,-1,-1]

def func(i, a, b):
    time.sleep(4)
    array[i] = a*b
    barrier.wait() #won't works without barrier



if __name__ == "__main__":
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=func, args=(i, i*2, i*3)))
    #Map step
    for t in threads:
        t.start()
    

    barrier.wait()
    r = 1
    #Reduce step
    for i in array:
        r = r + i
    print(r)
    for t in threads:
        t.join()


