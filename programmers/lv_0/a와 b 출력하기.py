# https://school.programmers.co.kr/learn/courses/30/lessons/181951
from typing import List

a, b = map(int, input().strip().split(' '))


def validate_input(value_list: List[int]) -> bool:
    for _value in value_list:
        if _value < -1000000 or _value > 1000000:
            return False
        continue
    return True


if validate_input([a, b]):
    print(f"a = {a}")
    print(f"b = {b}")


# 다른 답안
a, b = map(int, input().strip().split(' '))
print(f"a = {a}\nb = {b}")