n = int(input())

a = input()
for i in range(n-1):
    b = input()
    for i in range(len(a)):
        if a[i] != b[i]:
            a = f'{a[:i]}?{a[i + 1:]}'
    
print(a)