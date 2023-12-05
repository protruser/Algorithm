S,K = map(int, input().split())
answer = []
n = S//K

for _ in range(K):
    answer.append(n)
    
left = S - sum(answer)
for i in range(left):
    answer[i] += 1
    
number = 1
for i in answer:
    number*=i
    
print(number)