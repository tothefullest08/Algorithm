# https://school.programmers.co.kr/learn/courses/30/lessons/181950

a, b = input().strip().split(' ')
b = int(b)

if (1 <= len(a) <= 10) and (1 <= b <= 5):
    res = ''
    for i in range(b):
        res += a

    print(res)


if (1 <= len(a) <= 10) and (1 <= b <= 5):
    print(a * b)
