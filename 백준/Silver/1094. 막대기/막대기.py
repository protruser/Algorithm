X = int(input())
n = [64]

count = 1
while 1:
    if sum(n) > X:
        a = min(n)//2
        n.remove(min(n))
        if a + sum(n) >= X:
            n.append(a)
        else:
            n.append(a)
            n.append(a)
            
    if sum(n) == X:
        print(len(n))
        break