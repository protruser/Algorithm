def solution(arr):
    i = 1
    while len(arr) > i:
        i *= 2
        
    return arr + (i - len(arr))*[0]