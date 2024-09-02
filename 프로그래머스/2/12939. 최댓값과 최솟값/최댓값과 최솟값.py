def solution(s):
    answer= ''
    lst = s.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    
    answer += f'{min(lst)} '
    answer += f'{max(lst)}'
    return answer
    