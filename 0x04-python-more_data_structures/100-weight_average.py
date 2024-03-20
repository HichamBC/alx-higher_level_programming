#!/usr/bin/python3
def weight_average(my_list=[]):
    total_score = sum(map(lambda x: x[0] * x[1], my_list))
    total_weight = sum([x[1] for x in my_list])
    return total_score / total_weight
