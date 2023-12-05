while 1:
    A = input()
    if A == '0':
        break
    answer = 0
    answer += len(A) - 1 + 2
    for i in range(len(A)):
        if A[i] == '1':
            answer += 2
        elif A[i] == '0':
            answer += 4
        else:
            answer += 3
    print(answer)