import sys
N = int(input())
A = sorted(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
hap = 0
for i in range(N):
    hap += A[i]*max(B)
    B.remove(max(B))
    
print(hap)