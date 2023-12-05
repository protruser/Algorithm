N =int(input())

i = 6
i_list = []
while len(i_list) < 2*N:
    A = str(i)
    for n in range(len(A)):
        if A[-n-1] == '6':
            if n != 0:
                X = A[:-n-1]+'666'+A[-n:]
                if int(X) not in i_list:
                    i_list.append(int(X))
                    
            else:
                X = A[:-n-1]+'666'
                if int(X) not in i_list:
                    i_list.append(int(X))
            
    i += 1
    
i_list.sort()
print(i_list[N-1])