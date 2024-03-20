#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != "str":
        return 0

    rom_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            }
    res = 0
    for num in range(len(roman_string) - 1, -1, -1):
        current = rom_nums[roman_string[num]]
        if num != len(roman_string) - 1:
            prev = rom_nums[roman_string[num + 1]]
        if num != len(roman_string) - 1 and current < prev:
            res -= current
        else:
            res += current

    return res
