#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    else:
        args = sys.argv
        i = 0
        print(f"{len(args) - 1} {"arguments:" if len(args) - 1 > 1 else "argument:"}")
        for arg in args:
            if i == 0:
                i += 1
                continue
            print(f"{i}: {arg}")
            i += 1
