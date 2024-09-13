from collections import deque

def solution(numbers, k):
    numbers = deque(numbers)
    for i in range(k-1):
        numbers.rotate(-2)
    
    return numbers[0]
        
        