N = int(input())
lst = list(map(int, input().split()))
lst.sort()
s = 0
for i in range(N):
    s += sum(lst[:i+1])
print(s)