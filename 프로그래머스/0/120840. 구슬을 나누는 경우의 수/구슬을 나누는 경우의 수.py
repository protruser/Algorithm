def solution(balls, share):
    ball = 1
    a = 1
    b = 1
    
    for i in range(balls, 0, -1):
        ball *= i
        
    for i in range(share, 0, -1):
        a *= i
        
    for i in range(balls-share, 0, -1):
        b *= i
        
    return ball // (a * b)
