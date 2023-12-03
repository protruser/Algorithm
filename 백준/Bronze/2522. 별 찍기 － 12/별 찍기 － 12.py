N = int(input())

for i in range(1,2*N):
    a = '*'*N
    a = ' '*abs(N-i)+a[abs(N-i):]
    print(a)