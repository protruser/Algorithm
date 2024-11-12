def solution(nums):
    a = len(nums) // 2
    lst = list(set(nums))
    if a > len(lst):
        return len(lst)
    else:
        return a
    