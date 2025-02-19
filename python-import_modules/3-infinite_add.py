#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    sum = 0
    for number in args:
        sum += int(number)
    print(sum)
