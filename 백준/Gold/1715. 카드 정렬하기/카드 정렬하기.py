import sys
import heapq

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

answer = 0
lst = []
while heap:
    a = heapq.heappop(heap)
    lst.append(a)
        
    if len(lst) == 2:
        answer += sum(lst)
        heap.append(sum(lst))
        lst = []

print(answer)