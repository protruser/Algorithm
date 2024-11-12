def solution(nums):
    a = len(nums) // 2
    b = len(list(set(nums)))
    if a > b:
        return b
    else:
        return a
    