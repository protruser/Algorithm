import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
road = [[sys.maxsize for i in range(n+1)] for _ in range(n+1)]
graph = []

for _ in range(m):
    a,b,c = map(int, input().split())
    if road[a][b] > c:
        road[a][b] = c

for i in range(n+1):
    road[i][i] = 0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if road[i][j] > road[i][k] + road[k][j]:
                road[i][j] = road[i][k] + road[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if road[i][j] == sys.maxsize:
            road[i][j] = 0
        print(road[i][j],end=' ')
    print()