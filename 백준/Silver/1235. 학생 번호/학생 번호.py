import sys
N = int(input())

lst = []
for i in range(N):
    lst.append(sys.stdin.readline().rstrip())
    
answer = 1
for i in range(len(lst[0])-1,0,-1):
    st = set()
    for j in range(N):
        st.add(lst[j][i:])
    if len(lst) == len(st):
        print(answer)
        break
    else:
        answer += 1
        
if answer == len(lst[0]):
    print(answer)