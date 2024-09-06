def solution(arr):
    a = len(arr)
    b = len(arr[0])
    if a < b:
        for i in range(b-a):
            arr.append([0]*b)
    
    elif a > b:
        for i in range(len(arr)):
            for j in range(a-b):
                arr[i].append(0)
                
    return arr