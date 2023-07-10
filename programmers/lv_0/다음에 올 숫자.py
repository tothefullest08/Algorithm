def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1]//common[0])


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
print(solution([-2, -4, -8]))
