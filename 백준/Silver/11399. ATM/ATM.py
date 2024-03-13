N = int(input())
A = sorted(map(int, input().split()))

answer = 0
for i in range(N):
    answer += sum(A[:i+1])

print(answer)