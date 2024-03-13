import sys
N = int(input())
count = [0]*10001

for i in range(N):
    count[int(sys.stdin.readline())] += 1
    
for j in range(len(count)):
    for k in range(count[j]):
        print(j)