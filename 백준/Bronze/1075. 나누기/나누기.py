N = int(input())
F = int(input())

for i in range(100):
    if i < 10:
        i = f'0{i}'
        N = int(str(N)[:-2]+i)
    else:
        N = int(str(N)[:-2]+str(i))
    
    if N%F == 0:
        print(i)
        break