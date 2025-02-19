#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Exclude the script name from arguments
    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} {'arguments:' if num_args > 1 else 'argument:'}")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
