#!/usr/bin/python
import time

def boring(sleep_time=0):
    """
    Args:
    sleep_time (int): sleeping boring time.
    """
    print("this is a boring function")
    time.sleep(sleep_time)

def main():
    many_borings = 10
    for i, _ in enumerate(range(many_borings)):
        message = "{iteration} - boring stuff going on".format(iteration=str(i))
        print(message)
        boring(1)

if __name__ == '__main__':
    main()
