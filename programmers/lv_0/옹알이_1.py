speakable_words_list = ["aya", "ye", "woo", "ma"]

def permuate(arr, n):
    result = []
    if n == 0:
        return [[]]
    if n == 1:
        result = [[value] for value in arr]
        return result
    for i in range(len(arr)):
        value = arr[i]
        recursive_perm_res = permuate(arr[:i] + arr[i + 1:], n - 1)
        for res in recursive_perm_res:
            result.append([value] + res)

    return result


babbliable_list = []
for i in range(1, len(speakable_words_list) + 1):
    for babbling_permuation in permuate(speakable_words_list, i):
        babbliable_list.append(''.join(babbling_permuation))


def solution(babbling):
    answer = 0
    for word in babbling:
        if word in babbliable_list:
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"])) # 1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])) # 3


import itertools


babbliable_list_by_lib = []
for i in range(1, len(speakable_words_list) + 1):
    for babbling_permuation in itertools.permutations(speakable_words_list, i):
        babbliable_list_by_lib.append(''.join(babbling_permuation))


def solution2(babbling):
    answer = 0
    for word in babbling:
        if word in babbliable_list_by_lib:
            answer += 1

    return answer

print(solution2(["aya", "yee", "u", "maa", "wyeoo"])) # 1
print(solution2(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])) # 3