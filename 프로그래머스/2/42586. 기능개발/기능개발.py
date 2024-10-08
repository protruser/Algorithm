def solution(progresses, speeds):
    # progresses : 작업의 진도
    # speeds : 작업의 개발 속도
    answer = []
    idx = 0
    
    while (idx != len(progresses)):
        count = 0
        for oneday in range(idx, len(progresses)):
            progresses[oneday] += speeds[oneday]
        
        for i in range(idx, len(progresses)):
            if progresses[i] >= 100:
                idx += 1
                count += 1
            else:
                break
        
        if count != 0:
            answer.append(count)
                
            
    return answer