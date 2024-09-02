def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    if a == b:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
    else:
        if a > b:
            return 1
        else:
            return -1