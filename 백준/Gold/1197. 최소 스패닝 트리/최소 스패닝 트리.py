import sys
input = sys.stdin.readline
m,n = map(int, input().split())
graph = []
parent = [i for i in range(m+1)]
result = 0

for _ in range(n):
    a,b,c = map(int, input().split())
    graph.append((a,b,c))

graph = sorted(graph, key = lambda x : x[2])

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        a,b = b,a
    parent[b] = a
    

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

for a,b,c in graph:
    if find(a) != find(b):
        union(a,b)
        result += c

print(result)