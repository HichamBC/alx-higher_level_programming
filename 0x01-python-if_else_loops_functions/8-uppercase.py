#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        num = ord(letter)
        if num >= 97 and num <= 122:
            character = chr(num - 32)
        else:
            character = letter
        print("{}".format(character), end="")
    print()
