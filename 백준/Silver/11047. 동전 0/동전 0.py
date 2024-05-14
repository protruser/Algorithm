import sys
input = sys.stdin.readline
N,K = map(int, input().split())

coin = [int(input()) for _ in range(N)]
coin = sorted(coin, reverse = 1)

count = 0
for i in range(N):
    if K >= coin[i]:
        count += K//coin[i]
        K%=coin[i]
    
    if K == 0:
        break
    
print(count)