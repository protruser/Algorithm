import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
lst = [[] for _ in range(N+1)]
count = [0]*(N+1)
answer = deque()

for _ in range(M):
    A,B = map(int, input().split())
    lst[A].append(B)
    count[B] += 1

while len(answer) != N:
    for i in range(1,N+1):
        if count[i] == 0:
            count[i] = -1
            answer.append(i)
            for j in lst[i]:
                count[j] -= 1

for i in answer:
    print(i, end=' ')