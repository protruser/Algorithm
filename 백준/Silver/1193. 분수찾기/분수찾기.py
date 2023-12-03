X = int(input())

i = 0
while 1:
    i+= 1
    X = X - i
    if X <= 0:
        X +=i
        break
    
if i%2==0:
    print(X,'/',i-(X-1),sep='')
else:
    print(i-(X-1),'/',X,sep='')