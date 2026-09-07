#!/usr/bin/env python3.14t


import threading
import time

event = threading.Event()

data = None

def reader():
    global data
    file = "text.txt"
    with open(file, "r") as f:
        data = f.readline() # atomic
        if data:
            event.set()

def writer():
    event.wait()
    print(data)


if __name__ == "__main__":
    t_writer = threading.Thread(target=writer)
    t_writer.start()

    time.sleep(5)

    t_reader = threading.Thread(target=reader)
    t_reader.start()


    t_writer.join()
    t_reader.join()
