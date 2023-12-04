a = input().upper()
aski = []

for i in range(65,91):
    aski.append(a.count(chr(i)))
    
if aski.count(max(aski)) > 1:
    print('?')
else:
    print(chr(aski.index(max(aski))+65))