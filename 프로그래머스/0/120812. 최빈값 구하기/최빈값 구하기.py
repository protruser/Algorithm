def solution(array):
    lst = [0]*1001
    for i in array:
        lst[i] += 1
    
    judge = []
    a = max(lst)
    for i in range(len(lst)):
        if a == lst[i]:
            judge.append(i)
    
    if len(judge) != 1:
        return -1
    else:
        return judge[0]