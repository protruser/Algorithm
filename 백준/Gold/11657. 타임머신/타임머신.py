import sys
input = sys.stdin.readline
N,M = map(int, input().split())

graph = []
answer = [sys.maxsize]*(N+1)
answer[1] = 0
for _ in range(M):
    A,B,C = map(int, input().split())
    graph.append([A,B,C])

for _ in range(N-1):
    for a,b,c in graph:
        if answer[a] != sys.maxsize and answer[b] > answer[a] + c:
            answer[b] = answer[a] + c

flag = 1
for a,b,c in graph:
    if answer[a] != sys.maxsize and answer[b] > answer[a] + c:
        flag = 0

if flag:
    for i in answer[2:]:
        if i != sys.maxsize:
            print(i)
        else:
            print(-1)
else:
    print(-1)