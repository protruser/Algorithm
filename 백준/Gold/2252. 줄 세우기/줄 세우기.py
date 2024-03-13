import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int, input().split())
A = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    S,E = map(int, input().split())
    A[S].append(E)
    indegree[E] += 1

queue = deque()

for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    n = queue.popleft()
    print(n, end=' ')
    for i in A[n]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)