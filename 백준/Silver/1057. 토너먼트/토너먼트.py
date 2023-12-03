N,A,B = map(int, input().split())

n = 2
j = 0
answer = 1
while 1:
    if n*j < A <= n*(j+1) and n*j < B <= n*(j+1):
        break
    else:
        j += 1
    
    if n*j > N:
        answer += 1
        n*= 2
        j = 0
        
print(answer)