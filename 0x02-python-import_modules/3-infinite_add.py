#!/usr/bin/python3
def main():
    from sys import argv
    result = 0
    for arg in argv[1:]:
        result += int(arg)
    print(result)


if __name__ == "__main__":
    main()
