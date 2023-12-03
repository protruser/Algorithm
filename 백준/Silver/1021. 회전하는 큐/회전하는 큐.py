from collections import deque
answer = 0
N,M = map(int, input().split())
lst = list(map(int, input().split()))
queue = deque(i for i in range(1,N+1))

for i in lst:
    n = queue.index(i)
    if queue[0] == i:
        queue.popleft()
    else:
        if n <= len(queue)/2:
            queue.rotate(-n)
            answer += n
            queue.popleft()
        else:
            queue.rotate(len(queue)-n)
            answer += len(queue)-n
            queue.popleft()
            
print(answer)