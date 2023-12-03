N,M = map(int,input().split())

board = []
chess = ['WB'*32,'BW'*32]
answer = []

for _ in range(N):
    board.append(input())
    
for i in range(N-7):
    for j in range(M-7):
        wcount = 0
        ccount = 0
        word =''
        for a in range(8):
            for b in range(8):
                if a%2 == 0:
                    word += board[i+a][j+b]
                else:
                    word += board[i+a][j+7-b]
                    
        for k in range(64):
            if word[k] != chess[0][k]:
                wcount += 1
        
        for n in range(64):
            if word[n] != chess[1][n]:
                ccount += 1
                
        answer. append(min(wcount,ccount))
        
print(min(answer))