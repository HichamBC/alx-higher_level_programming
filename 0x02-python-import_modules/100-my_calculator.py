#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    from sys import exit, argv
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    print("{} {} {} = {}".format(a, op, b, operators[op](a, b)))


if __name__ == "__main__":
    main()
