N,M = map(int, input().split())

lst = [0 for i in range(N+1)]
for i in range(M):
  a,b,c = map(int, input().split())
  for j in range(a, b+1):
    lst[j] = c

for i in lst[1:]:
  print(i)