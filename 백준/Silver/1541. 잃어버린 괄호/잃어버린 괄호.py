n = input()
lst = list(n.split('-'))
answer = 0
for i in range(len(lst)):
    B = []
    B = list(lst[i].split('+'))
    for num in B:
        if i == 0:
            answer += int(num)

        else:
            answer -= int(num)

print(answer)