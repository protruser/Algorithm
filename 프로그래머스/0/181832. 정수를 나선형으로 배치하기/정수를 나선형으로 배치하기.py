from collections import deque

def solution(n):
    answer = [[0]*n for i in range(n)]
    
    num = n+1
    switch = 1
    idx = n-1
    a = 0
    b = n-1
    
    for i in range(1,n+1):
        answer[0][i-1] += i
        
        
    while switch != n:
        if switch%2 == 1:
            for i in range(n-switch):
                a += 1
                answer[a][b] += num
                num += 1
                
            for j in range(n-switch):
                b -= 1
                answer[a][b] += num
                num += 1
            
            switch += 1
                
        else:
            for i in range(n-switch):
                a -= 1
                answer[a][b] += num
                num += 1
            
            for j in range(n-switch):
                b += 1
                answer[a][b] += num
                num += 1
            switch += 1
                
    return answer
        
        
    
        