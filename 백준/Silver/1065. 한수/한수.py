N = int(input())

answer = 0
for i in range(1, N+1):
    i = str(i)
    if len(i) == 1:
        answer += 1
    elif len(i) == 2:
        answer += 1
    else:
        if int(i[0])-int(i[1]) == int(i[1])-int(i[2]):
            answer += 1
    
print(answer)