import sys
a,b = map(int, input().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

C = A + B
D = list(set(A+B))

print(2*len(D)-len(C))