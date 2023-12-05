lst = ['a','e','i','o','u']
while 1:
    n = input()
    count = 0
    if n == '#':
        break
    
    n = n.lower()
    for i in lst:
        for j in n:
            if i == j:
                count += 1
                
    print(count)