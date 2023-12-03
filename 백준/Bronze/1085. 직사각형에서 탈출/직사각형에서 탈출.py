x,y,w,h = map(int,input().split())

A = h-y
B = y-0
C = w-x
D = x-0

print(min(A,B,C,D))