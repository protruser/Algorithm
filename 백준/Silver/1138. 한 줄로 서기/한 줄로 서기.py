N = int(input())
line = [0]*N
B = list(map(int, input().split()))

for i in range(N):
    count = 0
    for j in range(N):
        if count == B[i]:
            a = j
            break
        
        if line[j] == 0:
            count += 1
    
    if line[a] == 0:
        line[a] = i+1
    else:
        n = 1
        while 1:
            if line[a+n] == 0:
                line[a+n] = i+1
                break
            else:
                n += 1
    
for i in line:
    print(i, end =' ')