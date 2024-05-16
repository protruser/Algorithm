N,K = map(int, input().split())
answer = 1
for i in range(K):
    answer*= (N-i)
for i in range(K):
    answer /= K-i
print(int(answer))