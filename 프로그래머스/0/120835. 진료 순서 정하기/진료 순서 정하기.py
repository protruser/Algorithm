def solution(emergency):
    answer = [0]*len(emergency)
    
    n = 1
    while n != len(emergency)+1:
        a = max(emergency)
        for i in range(len(emergency)):
            if emergency[i] == a:
                answer[i] += n
                emergency[i] = 0
                n += 1
                
    return answer
        
        