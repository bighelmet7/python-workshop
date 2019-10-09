#!/usr/bin/python

def fizz_buzz(n_numbers):
    """
    Args:
    n_numbers (int): total of numbers to be treated.

    Prints Fizz when a number is multiple of 3, Buzz when its for 5 and
    FizzBuzz when its of both. Otherwise print the number.
    """
    for i in range(1, n_numbers + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def main():
    fizz_buzz(15)

if __name__ == '__main__':
    main()
