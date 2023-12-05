N = int(input())
words = []
count = 0

for i in range(N):
    words.append(input().lower())

for i in range(N):
    count = 0
    for j in range(len(words[i])-1-count):
        if words[i][j-count] == words[i][j+1-count]:
            words[i] = words[i][:j-count]+words[i][j+1-count:]
            count = count + 1
        else:
            pass

number = 0
compare = []

for i in range(N):
    for word in words[i]:
        if word not in compare:
            compare.append(word)
            
    sort = ''.join(compare)
    if words[i] == sort:
        number = number + 1

    compare = []

print(number)