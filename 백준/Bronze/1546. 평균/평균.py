n = int(input())
lst = list(map(int, input().split()))
lst2 = []
M = max(lst)

for i in range(n):
    lst[i] = lst[i]*100/M

print(sum(lst)/n)