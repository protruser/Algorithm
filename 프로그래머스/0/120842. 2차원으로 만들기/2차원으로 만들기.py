def solution(num_list, n):
    answer = [[] for i in range(len(num_list)//n)]
    a = 0
    
    for i in range(len(num_list)//n):
        for j in range(n):
            answer[i].append(num_list[a])
            a += 1
    return answer