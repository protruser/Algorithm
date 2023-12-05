import sys
N = int(input())
lst = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)

same = [0]*N
for i in range(N):
    p =set()
    for j in range(5):
        for k in range(N):
            if lst[i][j] == lst[k][j]:
                if i != k:
                    p.add(k)
    same[i] += len(p)

for i in range(len(same)):
    if same[i] == max(same):
        print(i+1)
        break