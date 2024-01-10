def solution(food):
    answer = ''
    for i in range(len(food)-1,0,-1):
        a = (food[i]-food[i]%2) //2
        answer = a*str(i) + answer + a*str(i)
        
    n = len(answer)//2
    answer = answer[:n] + '0' + answer[n:]
    return answer
    