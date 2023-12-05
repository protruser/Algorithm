N = int(input())

guitar = {}
for i in range(N):
    a = input()
    n = 0
    for i in a:
        try:
            n += int(i)
        except:
            pass
    guitar[a] = n

answer = sorted(guitar.items(), key = lambda x : (len(x[0]),x[1],x[0]))
for i,j in answer:
    print(i)