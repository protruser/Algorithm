word = input().upper()
aski = []

for i in range(26):
    aski.append(word.count(chr(65+i)))

if aski.count(max(aski))>1:
    print('?')
else:
    print(chr(aski.index(max(aski))+65))
