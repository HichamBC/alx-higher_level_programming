#!/usr/bin/python3
def main():
    from sys import argv
    count = len(argv) - 1
    if count >= 1:
        if count == 1:
            print("{} argument:".format(count))
        else:
            print("{} arguments:".format(count))

        for i, arg in enumerate(argv[1:], 1):
            print("{}: {}".format(i, arg))
    else:
        print("{} arguments.".format(count))


if __name__ == "__main__":
    main()
