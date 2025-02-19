#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Exclude the script name from arguments
    num_args = len(argv)

    # Print the number of arguments
    print(
        f"Number of argument{'(s)' if num_args != 1 else ''}: {num_args}{':' if num_args > 0 else '.'}"
    )

    # Print each argument with its position
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
