from collections import deque

def dfs(graph,v,visited):
    visited[v] = True
    answer.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        answer.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N,M,V = map(int,input().split())
graph = []
for i in range(N+1):
    graph.append([])
    
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
    
answer = []
visited = [False]*(N+1)

dfs(graph,V,visited)
for i in answer:
    print(i, end=' ')

visited = [False]*(N+1)
answer = []

bfs(graph,V,visited)
print()
for i in answer:
    print(i, end=' ')