A,B = map(str, input().split())

answer = 0
if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            answer += 1
    print(answer)
    
else:
    if len(A) > len(B):
        A,B = B,A
    answer = len(B)
    n = len(B)-len(A)+1
    
    for i in range(n):
        X = ' '*i + A + ' '*(n-i)
        compare = 0
        
        for j in range(len(B)):
            if X[j] != B[j]:
                compare += 1
                
        if compare <= answer:
            answer = compare
            
    print(answer - n + 1)