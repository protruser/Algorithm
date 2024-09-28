N = int(input())

for i in range(N):
  n = int(input())
  num1, num2 = 0, 1
  if n == 0:
    print(1, 0)
  else:
    for i in range(n-1):
      num1, num2 = num2, num1 + num2
    
    print(num1, num2)