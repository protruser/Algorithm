N = int(input())

def f(word,i,j,count):
    if i >= j:
        return 1, count
    
    if word[i] == word[j]:
        count += 1
        return f(word,i+1,j-1,count)
    else:
        return 0, count
    
for i in range(N):
    A = input()
    tup = f(A,0,len(A)-1,1)
    print(tup[0],tup[1])