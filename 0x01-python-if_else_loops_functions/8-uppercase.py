#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        num = ord(letter)
        if num >= 97 and num <= 122:
            character = chr(num - 32)
            print(character, end="")
        else:
            print(letter, end="")
    print()
