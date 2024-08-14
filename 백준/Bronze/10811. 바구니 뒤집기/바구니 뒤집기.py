N,M = map(int, input().split())

lst = [i for i in range(N+1)]

for i in range(M):
  a,b, = map(int, input().split())
  basket = lst[a:b+1]
  basket.reverse()
  lst[a:b+1] = basket

for i in lst[1:]:
  print(i, end=' ')