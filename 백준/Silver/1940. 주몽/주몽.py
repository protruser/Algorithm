import sys

N = int(input())
M = int(input())
lst = list(map(int, sys.stdin.readline().split()))

a,b = 0,N-1
cnt = 0
lst = sorted(lst)

while a != b:
    if lst[a]+lst[b] < M:
        a += 1
    elif lst[a]+lst[b] > M:
        b -= 1
    else:
        cnt += 1
        a += 1

print(cnt)