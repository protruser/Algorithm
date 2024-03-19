a,b = map(int, input().split())

count = 1
while b != a:
    try:
        if str(b)[-1] == '1':
            b = int(str(b)[:-1])
            count += 1
        elif b%2 ==0:
            b//=2
            count += 1
        else:
            break
    except:
        break

if a == b:
    print(count)
else:
    print(-1)