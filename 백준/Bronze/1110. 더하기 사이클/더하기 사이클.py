n = int(input())

answer = n
count = 0
while 1:
    if n == 0:
        n = 0
    elif n < 10:
        n = int(str(n)*2)
    else:
        a = int(str(n)[0])+int(str(n)[1])
        n = int(f'{str(n)[1]}{str(a)[-1]}')
        
    count += 1
    if n == answer:
        break
    
print(count)