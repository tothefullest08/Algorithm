# https://school.programmers.co.kr/learn/courses/30/lessons/181952
string_input = input()

while True:
    if 1 <= len(string_input) <= 1000000:
        print(string_input)
        break
    else:
        continue
