import sys
T = int(input())

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    a = a%10
    if a == 1:
        print(1)
        
    elif a == 2:
        if b%4 == 0:
            print(6)
        elif b%4 == 1:
            print(2)
        elif b%4 == 2:
            print(4)
        else:
            print(8)
            
    elif a == 3:
        if b%4 == 0:
            print(1)
        elif b%4 == 1:
            print(3)
        elif b%4 == 2:
            print(9)
        else:
            print(7)
            
    elif a == 4:
        if b%2 == 0:
            print(6)
        else:
            print(4)
            
    elif a == 5:
        print(5)
        
    elif a == 6:
        print(6)
        
    elif a == 7:
        if b%4 == 0:
            print(1)
        elif b%4 == 1:
            print(7)
        elif b%4 == 2:
            print(9)
        else:
            print(3)
            
    elif a == 8:
        if b%4 == 0:
            print(6)
        elif b%4 == 1:
            print(8)
        elif b%4 == 2:
            print(4)
        else:
            print(2)
            
    elif a == 9:
        if b%2 == 0:
            print(1)
        else:
            print(9)
            
    else:
        print(10)