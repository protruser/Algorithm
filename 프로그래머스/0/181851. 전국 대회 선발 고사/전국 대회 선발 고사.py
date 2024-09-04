def solution(rank, attendance):
    lst = [10000, 100, 1]
    idx = 0
    answer = []
    
    for i in range(1,len(rank)+1):
        for j in range(len(rank)):
            if i == rank[j] and attendance[j] == True:
                answer.append(lst[idx]*j)
                idx += 1
                break
        
        if len(answer) == 3:
            return sum(answer)
            
        
                
        