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
    boring(1)

if __name__ == '__main__':
    main()
