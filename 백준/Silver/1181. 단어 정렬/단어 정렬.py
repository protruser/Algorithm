import sys
N = int(input())
A = []

for i in range(N):
    A.append(input())
    
A = list(set(A))
A.sort()

n = 1
B = []
while  len(B) < len(A):
    for i in A:
        if len(i) == n:
            B.append(i)
    
    n += 1
    
for i in B:
    print(i)