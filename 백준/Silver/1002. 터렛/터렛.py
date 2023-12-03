N = int(input())
for _ in range(N):
    a,b,r1,c,d,r2 = map(int, input().split())
    if a == c and b == d and r1 == r2:
        print(-1)
    elif a == c and b == d:
        print(0)
    elif abs(r2-r1) == ((a-c)**2 + (b-d)**2)**0.5:
        print(1)
    elif abs(r2-r1) > ((a-c)**2 + (b-d)**2)**0.5:
        print(0)
    elif r1+r2 > ((a-c)**2 + (b-d)**2)**0.5:
        print(2)
    elif r1+r2 == ((a-c)**2 + (b-d)**2)**0.5:
        print(1)
    elif r1+r2 < ((a-c)**2 + (b-d)**2)**0.5:
        print(0)