def solution(strArr):
    lst = [0]*31
    for i in strArr:
        lst[len(i)] += 1
    return max(lst)