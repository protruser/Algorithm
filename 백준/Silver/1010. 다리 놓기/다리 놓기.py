T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    answer = 1
    for j in range(N):
        answer *= (M-j)
    
    for k in range(N):
        answer //= (N-k)
        
    print(int(answer))