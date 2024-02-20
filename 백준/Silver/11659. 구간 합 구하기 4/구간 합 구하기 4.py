import sys
input = sys.stdin.readline

M,N = map(int,input().split())
lst = list(map(int, input().split()))
lst2 = [0] * (M+1)

for i in range(M):
    lst2[i+1] = lst2[i] + lst[i]

for i in range(N):
    i,j = map(int,input().split())
    print(lst2[j]-lst2[i-1])