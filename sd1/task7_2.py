#!/usr/bin/env python3.14t

import threading
import time
import itertools


def func(barrier, semaphore, num_phil, left_fork, right_fork):
    print(f"Philosopher {num_phil} is at the table")
    barrier.wait()
    with semaphore:
        with left_fork:
            print(f"Philosopher {num_phil} took left fork")
            with right_fork:
                print(f"Philosopher {num_phil} took right fork and started eat")
            print(f"Philosopher {num_phil} released right fork")
        print(f"Philosopher {num_phil} released left fork")

if __name__ == "__main__":
    # Five philosofers (only mutex)
    for i in itertools.permutations(range(5)):
        print(i)
        barrier = threading.Barrier(5)
        semaphore = threading.Semaphore(4) # Special moment!
        forks = [threading.Lock() for _ in range(5)]
        threads = []
        threads.append(threading.Thread(target=func, args=(barrier, semaphore, 0, forks[0], forks[1])))
        threads.append(threading.Thread(target=func, args=(barrier, semaphore, 1, forks[1], forks[2])))
        threads.append(threading.Thread(target=func, args=(barrier, semaphore, 2, forks[2], forks[3])))
        threads.append(threading.Thread(target=func, args=(barrier, semaphore, 3, forks[3], forks[4])))
        threads.append(threading.Thread(target=func, args=(barrier, semaphore, 4, forks[4], forks[0])))


        for t in i:
            threads[t].start()

        for t in threads:
            t.join()

        print('finish')

