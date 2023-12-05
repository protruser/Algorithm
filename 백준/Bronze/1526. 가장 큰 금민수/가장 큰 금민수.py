N=int(input())
for n in range(N,3,-1):
    switch = 0
    for i in str(n):
        if i == '4' or i == '7':
            switch += 1
        else:
            break
    if switch == len(str(n)):
        print(n)
        break